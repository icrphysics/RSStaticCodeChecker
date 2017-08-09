################################################################################
# +--------------------------------------------------------------------------+ #
# |                               +----+                                     | #
# |                               |INFO|                                     | #
# |                               +----+                                     | #
# |                                                                          | #
# | Error types can be ignored in the next line by using this:               | #
# |                                                                          | #
# | #@ignore_error_type(error_type)                                          | #
# |                                                                          | #
# | You can also concatenate error types in this command:                    | #
# |                                                                          | #
# | #@ignore_error_type(attribute_error, parameter_error)                    | #
# |                                                                          | #
# | A variable can be ignored for the whole file by using this:              | #
# |                                                                          | #
# | #@ignore_variable(patient)                                               | #
# |                                                                          | # 
# | where "patient" is the variable to ignore.                               | # 
# |                                                                          | #
# | A variable can also be ignored only for a specific error                 | #
# | types:                                                                   | #
# |                                                                          | #
# | #@ignore_variable(patient, error_types=[attribute_error])                | #
# |                                                                          | #
# | Several macros can be written in one line by separating them             | #
# | with the "|" character.                                                  | #
# |                                                                          | #
# | #@ignore_error_type(attribute_error)|@ignore_error_type(parameter_error) | #
# |                                                                          | #
# +--------------------------------------------------------------------------+ #
################################################################################

def get_all_commands(raw):
    """
    Splits the given string at '|' to return all the contained ignore statements
    @param raw: The line of code that is a comment without the '#', (e.g. `@ignore_...(...)|@ignore_...`)
    """
    splitting = raw.split("|")
    return splitting

def get_variables_to_ignore(c, error_type):
    """
    Returns all the variables that should be ignored by this piece of macro
    @param c: The code of the comment without the '#'
    @param error_type: The error type that it should look for
    @returns a string list containing all variable names that should be ignored
    """
    splitting = get_all_commands(c)
    variables_to_ignore = []
    for s in splitting:
        variables = get_variables_single_cmd(s, error_type)
        variables_to_ignore.extend(variables)
    return variables_to_ignore

def get_variables_single_cmd(c, error_type):
    """
    Gives all ignore variables in the given single command
    @param c: A single command that looks like this @ignore_var(...)
    @param error_type: The error type it should look for
    @returns a string list containing all variable names that should be ignored
    """
    import ast, json
    if not c.startswith("@"):
        return []
    try:
        node_result = ast.parse(c[1:])
        import ast_to_json
        json_dump = ast_to_json.ast2json(node_result)
        d = json.loads(json_dump)
        if not d.get("body") or not len(d.get("body")) > 0:
            return []
        d_body = d.get("body")[0].get("value")
        if not d_body.get("_PyType") == "Call":
            return []
        if not d_body.get("func"):
            return []
        
        if not d_body.get("func").get("_PyType") == "Name":
            return []
        
        if not d_body.get("func").get("id") == "ignore_variable": #TODO config
            return []

        args = d_body.get("args")
        if not args:
            return []
        variables = []
        for arg in args:
            if arg.get("_PyType") != "Name":
                continue
            variables.append(arg.get("id"))
        
        kwargs = d_body.get("keywords")
        if not kwargs:
            return variables
        error_types = []
        for kwarg in kwargs:
            if kwarg.get("arg") == "error_types":
                values = kwarg.get("value").get("elts")
                for v in values:
                    if v.get("id"):
                        error_types.append(v.get("id"))
        if error_type in error_types:
            return variables
        return []
    except:
        return []

def get_error_types_to_ignore(c):
    """
    Returns a list of all error types that should be ignored in the next line of code for a given string containing one or more macro commands
    @param c: The line of code that is a comment without the '#', (e.g. `@ignore_...(...)|@ignore_...`)
    @returns: A string list of all the error types that should be ignored in the next line of code
    """
    splitting = get_all_commands(c)
    types_to_ignore = []
    for s in splitting:
        errortypes = get_error_types_to_ignore_single_cmd(s)
        types_to_ignore.extend(errortypes)
    return types_to_ignore

def get_error_types_to_ignore_single_cmd(c):
    """
    Returns a list of all error types that should be ignored in the next line of code for a given list string containing exactly one commands
    @param c: The single command (e.g. `@ignore_...`)
    @returns: A string list of all the error types that should be ignored in the next line of code
    """
    import ast, json
    if not c.startswith("@"):
        return []
    try:
        node_result = ast.parse(c[1:])
        import ast_to_json
        json_dump = ast_to_json.ast2json(node_result)
        d = json.loads(json_dump)
        error_types_to_ignore = []
        if not d.get("body") or not len(d.get("body")) > 0:
            return []
        d_body = d.get("body")[0].get("value")
        
        if not d_body.get("_PyType") == "Call":
            return []
        
        if not d_body.get("func"):
            return []
        
        if not d_body.get("func").get("_PyType") == "Name":
            return []
        
        if not d_body.get("func").get("id") == "ignore_error_type": #TODO config
            return []
        
        args = d_body.get("args")
        if not args:
            return []
        
        for arg in args:
            
            if arg.get("_PyType") != "Name":
                continue
            error_types_to_ignore.append(arg.get("id"))
        return error_types_to_ignore
    except:
        return []