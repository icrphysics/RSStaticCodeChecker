def score_generic(d, attr_name):
    """
    Get's the score for all attributes except a base attribute.
    It actually just checks the json dict that represents the AST node on whether it is an attribute with the given value.
    If in attr_name an array placeholder is given, it will be checked whether the given node is a list index specification (e.g. "[i+1]").
    @param d: The dict representing the AST node
    @param attr_name: The attribute name the dict should represent
    @returns The score (sys.maxint if wrong or 0.0 if right)
    """
    import sys
    score = sys.maxint

    if attr_name != "[]":
        #for access via something.attr
        if d.get("_PyType") == "Attribute":
            if d.get("attr") == attr_name:
                return 0
        #for access via something["attr"]
        elif d.get("_PyType") == "Subscript":
            if d.get("slice").get("_PyType") == "Index":
                if d.get("slice").get("value").get("_PyType") == "Str" and d.get("slice").get("value").get("s") == attr_name:
                    return 0
        return sys.maxint
    else:
        if not d.get("_PyType") == "Subscript":
            return sys.maxint
        else:
            score = 0
    return score