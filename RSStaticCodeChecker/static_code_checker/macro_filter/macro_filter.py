import uuid
def filter_dict(code, d, error_type, returnValue=None):
    new_d_error_type_filter = remove_lines_from_dict(d, _get_lines_to_filter(code, error_type))
    new_d_variable_filter = remove_variables_from_dict(new_d_error_type_filter, __get_variables_to_filter(code, error_type))
    if returnValue != None:
        returnValue["return"] = new_d_variable_filter
        return
    return new_d_variable_filter

def remove_variables_from_dict(d, variables):
    if isinstance(d, dict):
        new_d = {}
        for key in d:
            sub_dict = d.get(key)
            modified_sub_dict = remove_variables_from_dict(sub_dict, variables)
            new_d[key] = modified_sub_dict
        if d.get("_PyType") == "Name" and d.get("id") in variables:
            new_d["id"] = str(uuid.uuid4())
        return new_d
    elif isinstance(d, list):
        new_d = []
        for sub_dict in d:
            modified_sub_dict = remove_variables_from_dict(sub_dict, variables)
            new_d.append(modified_sub_dict)
        return new_d
    return d

def __get_variables_to_filter(code, error_type):
    import comment_parser
    lines = list(iter(code.splitlines()))
    variables = []
    for i, line in enumerate(lines):
        core = line.strip()
        if not core.startswith("#"):
            continue
        variables.extend(comment_parser.get_variables_to_ignore(core[1:], error_type))
    #print "DEBUG: For {} ignore variables {}".format(error_type, variables)
    return variables

def remove_lines_from_dict(d, lines):
    if isinstance(d, dict):
        if d.get("lineno") and int(d.get("lineno")) in lines:
            return {
                "__ignored" : True
            }
        new_d = {}
        for key in d:
            sub_dict = d.get(key)
            modified_sub_dict = remove_lines_from_dict(sub_dict, lines)
            new_d[key] = modified_sub_dict
        return new_d
    elif isinstance(d, list):
        new_d = []
        for sub_dict in d:
            modified_sub_dict = remove_lines_from_dict(sub_dict, lines)
            new_d.append(modified_sub_dict)
        return new_d
    return d

def _get_lines_to_filter(code, error_type):
    import comment_parser
    lines = list(iter(code.splitlines()))
    ignore = False
    filter_lines = []
    for i, line in enumerate(lines):
        core = line.strip()
        if not core.startswith("#"):
            continue
        error_types = comment_parser.get_error_types_to_ignore(core[1:])
        if error_type not in error_types:
            continue
        filter_lines.append(i+2) #because the lineno starts counting with 1
    
    #print "DEBUG: For {} ignore lines {}".format(error_type, str(filter_lines))
    return filter_lines