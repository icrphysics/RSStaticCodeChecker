def get_score(d):
    """
    checks the score for a dict representing the AST node for the base entry 'MachineDB'
    """
    import sys, re
    score = sys.maxint
    if not d.get("_PyType") == "Name":
        return sys.maxint
    if re.match("^machine_?db$", d.get("id")) != None:
        score = min(score, 0)
    if re.match(".*machine_?db.*(?<!s)$", d.get("id")) != None:
        score = min(score, 1)
    return score