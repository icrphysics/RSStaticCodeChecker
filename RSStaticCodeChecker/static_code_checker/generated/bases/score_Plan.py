def get_score(d):
    """
    checks the score for a dict representing the AST node for the base entry 'Plan'
    """
    import sys, re
    score = sys.maxint
    if not d.get("_PyType") == "Name":
        return sys.maxint
    if re.match("^(P|p)(L|l)(A|a)(N|n)$", d.get("id")) != None:
        score = min(score, 0)
    if re.match("(P|p)(L|l)(A|a)(N|n).*(?<!s)$", d.get("id")) != None:
        score = min(score, 1)
    return score