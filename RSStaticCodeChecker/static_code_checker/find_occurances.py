import json
import importlib
import sys
import ast
import ast_to_json
import col_to_calculator
import multiprocessing
import threading

print_enabled = False

no_of_processes = 4

def find_in_file(file, generate=False):
    """
    Finds all potential errors in a code.
    @param file: The filepath to the file that should be checked
    @returns: A list of results
    """
    if generate:
        import prepare_for_checks
        prepare_for_checks.prepare()
    
    results = []
    with open(file, 'r') as myfile:
        data=myfile.read()
        temp_results = find_in_code(data)
        for r in temp_results:
            r["file"] = file
        results.extend(temp_results)
    return results

def post_processing(results):
    new_results = []
    for result in results:
        new_dict = dict(result)
        error_code = new_dict.get("error_code")
        if new_dict.get("error_type") and new_dict.get("error_type") == "attribute_error":
            #attribute_error
            wrong_attribute = error_code.split(".")[-1]
            if wrong_attribute == "[]":
                new_dict["description"] = "The object '{}' is accessed like a list which could cause errors.".format(".".join(error_code.split(".")[:-1]))
            else:
                new_dict["description"] = "Object '{}' has no attribute '{}'".format(".".join(error_code.split(".")[:-1]), wrong_attribute)
        else:
            #parameter_error
            new_dict["description"] = "You seem to either use wrong or not enough parameters for method '{}(...)'. Check the documentation for further details.".format(error_code.split(".")[-1])
        new_results.append(new_dict)
    return new_results

def find_in_code(code, version=None):
    """
    Finds all potential errors in a code.
    @param code: The code as a string
    @returns: A list of results
    """
    
    try:
        node = ast.parse(code)
    except:
        return []
    ast.fix_missing_locations(node)
    json_str = ast_to_json.ast2json(node)


    as_dict = json.loads(json_str)
    
    from macro_filter import macro_filter


    attribute_check_dict = macro_filter.filter_dict(code, as_dict, "attribute_error")
    parameter_check_dict = macro_filter.filter_dict(code, as_dict, "parameter_error")


    #for all argument changes
    
    
    results = []
    import os
    attribute_base = []
    wildcards = []
    package_directory = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(package_directory, 'information', 'all_attributes.json')) as f:
        attribute_base = json.loads(f.read())
    with open(os.path.join(package_directory, 'information', 'attr_wildcards.json')) as f:
        wildcards = json.loads(f.read())
    
    results = check_dict_for_attributes(attribute_check_dict, attribute_base, wildcards)
    results.extend(parameter_check(code, parameter_check_dict, print_enabled))
    results = post_processing(results)
    return results


def parameter_check(code, parameter_check_dict, print_enabled=False, returnValue=None):
    """
    Will execute parameter_check_ast() on the given dict and return the union of results for all argument_change_xxx modules in the "generated" folder.
    @param code: The raw code
    @param parameter_check_dict: AST node (in the form of a dict) - basically: json.loads(ast_to_json.ast2json(ast.parse("Code")))
    @param print_enabled: Is print enabled?
    @param returnValue: If is not None then nothing will be returned but the given "returnValue" (which should be a list) will be extended with what would
                        otherwise be the return value
    @returns: the union of results for all argument_change_xxx modules in the "generated" folder
    """
    i = 0
    argument_changes = []
    while True:
        #Not a nice solution...
        try:
            importlib.import_module("generated.argument_change_{}".format(i))
        except Exception, e:
            break
        argument_changes.append(i)
        i += 1

    results = []
    for j in range(i):
        results.extend(parameter_check_ast(code, parameter_check_dict, j))
        if print_enabled:
            sys.stdout.write("\r")
            sys.stdout.write("{:.0%}".format((float(j)/float(i)) * 0.5 + 0.5))
            sys.stdout.flush()
    

    
    if print_enabled:
        sys.stdout.write("\r")    
    if returnValue != None:
        returnValue.extend(results)
        return
    return results


def parameter_check_ast(raw, d, id):
    """
    Finds all potential parameter errors in an AST node (in the form of a dict).
    @param raw: The raw code, for performance reasons (shallow scan of the code)
    @param d: AST node (in the form of a dict) - basically: json.loads(ast_to_json.ast2json(ast.parse("Code")))
    @param id: The id of the check
    @returns: A list of results for wrong parameter usage
    """
    
    threshold = 4 #TODO: Don't hardcode
    
    i = importlib.import_module("generated.argument_change_{}".format(id))
    
    results = []

    if not i.easyCheck(raw):
        return []
    
    results.extend(check_dict(d, i, threshold))
    
    for result in results:
        result["test_id"] = id

    return results


def check_dict_for_attributes(d, attribute_base, wildcards, returnValue=None):
    """
    Will execute attribute_checker.results_for_dict() for the given dict and return the results.
    So it's basically a wrapper function for attribute_checker.results_for_dict
    @param d: The dict that should be checked
    @param attribute_base: All possible attribute combinations. (Should most likely be a json.loads of the information/all_attributes.json file)
    @param returnValue: If is not None then nothing will be returned but the given "returnValue" (which should be a list) will be extended with what would
                        otherwise be the return value.
    @returns: A list of results for invalid attribute combinations
    """
    import attribute_checker
    results = attribute_checker.results_for_dict(d, attribute_base, wildcards, [])
    if returnValue != None:
        returnValue.extend(results)
        return
    return results


def check_dict(d, module, threshold):
    """
    Checks a dict with a specific parameter test
    @param d: AST node (in the form of a dict) - basically: json.loads(ast_to_json.ast2json(ast.parse("Code")))
    @param module: the module which should be used to check the code (must contain a scoreForDict() method)
    @param threshold: The threshold to use
    @returns a list of found results
    """
    results = []

    if isinstance(d, dict):
        for k in d:
            results.extend(check_dict(d[k], module, threshold))
    elif isinstance(d, list):
        for k in d:
            results.extend(check_dict(k, module, threshold))

    score = module.scoreForDict(d)
    if score <= threshold:
        info = module.get_info()
        result = {
            "score": score,
            "value": d,
            "error_type": "parameter_error",
            "error_code": "{}.{}".format(info.get("base"), info.get("method")),
            "info": info
        }
        if d.get("lineno"):
            result["lineno"] = d.get("lineno")
        if d.get("col_offset"):
            result["col_offset"] = d.get("col_offset")
            result["col_offset_to"] = col_to_calculator.get_to_col_offset(result.get("value"))
        results.append(result)

    
    return results





##############################
########## CMD PART ##########
##############################
import sys, os
def main():
    """
    The command line tool implementation of the functions in this script.
    Arguments:
        - f: The file that should be checked

    Try to not use this implementation but rather the static_code_checker_client implementation with a setup of the static_code_checker_server.
    """
    import argparse, json
    parser = argparse.ArgumentParser()
    parser.add_argument("f")
    args = parser.parse_args()
    blockPrint()
    results = find_in_file(args.f)
    enablePrint()
    print json.dumps(results)

def blockPrint():
    """
    Disables all stdout prints.
    Helpfull for creating a command line tool
    """
    sys.stdout = open(os.devnull, 'w')

def enablePrint():
    """
    Enables all stdout prints.
    Helpfull for creating a command line tool
    """
    sys.stdout = sys.__stdout__


if __name__ == "__main__": main()