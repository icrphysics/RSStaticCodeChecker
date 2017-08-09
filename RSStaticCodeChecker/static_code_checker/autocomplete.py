import importlib, sys
from checker_config import config as conf
def get_completions(document, line, x, returnFinal = False):
    """
    An attribute auto completion implementation using ./information/all_attributes.json.
    @param document: The full code of the document
    @param line: The line in the code
    @param x: The cursor position in the line
    @param returnFinal: If set to true the "final" parsing will be returned as a second return value
    @returns All attribute infos that could be what the user wanted to entry. "patient.C" would return ["patient.Cases", "patient.Cases.[]", patient.Cases.[].Name", ...]
    """
    database = []
    import json
    import os 
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(dir_path, "information", "all_attributes.json"), "r") as f:
        database = json.loads(f.read())


    l = document.splitlines()[line]
    regex = r'[0-9a-zA-Z_\.\[\]\(\)\"\']*$'
    front_part = l[:x]
    
    import re
    results = re.findall(regex, front_part)
    search_string = max(results, key=len)


    # REGEX MAGIC IS FASTER THAN AST PARSING!
    arrayReplace = r'\[([0-9a-zA-Z\(\)\"\'\.]|(\[\]))+\]'
    bracket_regex = re.compile(arrayReplace)
    
    prev_line = search_string
    next_line = re.sub(arrayReplace, ".[]", prev_line)
    while next_line != prev_line:
        prev_line = next_line
        next_line = re.sub(arrayReplace, ".[]", prev_line)
    
    final = next_line
    
    obj_type = get_object_type(final)
    if obj_type is None:
        return [], final

    final = re.sub(r'^[a-zA-Z_0-9]+\.', "{}.".format(obj_type), final)


    final_search_regex = "^{}".format(final.replace(".", r'\.').replace("[", r'\[').replace("]", r'\]'))
    compiled_search = re.compile(final_search_regex)

    matches = filter(compiled_search.match, database)
    if returnFinal:
        return matches, final
    return matches

def get_object_type(final):
    #simulate AST
    d = {
        "id": final.split(".")[0],
        "_PyType": "Name"
    }
    for obj_type in conf.object_types:
        i = importlib.import_module("generated.bases.score_{}".format(obj_type))
        score = i.get_score(d)
        if score != sys.maxint:
            return obj_type
    return None

def get_completion_words(document, line, x):
    completions, final = get_completions(document, line, x, True)
    attr_depth = len(final.split(".")) - 1
    words = set()
    for completion in completions:
        s = completion.split(".")
        if s[attr_depth] == "[]":
            return None
        words.add(s[attr_depth])
    return list(words)


import sys, os
def main():
    import argparse, json
    parser = argparse.ArgumentParser()
    parser.add_argument("code")
    parser.add_argument("line")
    parser.add_argument("col")
    args = parser.parse_args()
    blockPrint()
    results = get_completion_words(args.code, args.line, args.col)
    enablePrint()
    print json.dumps(results)


# Disable
def blockPrint():
    sys.stdout = open(os.devnull, 'w')

# Restore
def enablePrint():
    sys.stdout = sys.__stdout__


if __name__ == "__main__": main()

