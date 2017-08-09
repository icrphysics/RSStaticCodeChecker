def get_score(d):
    """
    checks the score for a dict representing the AST node for the base entry 'BeamSet'
    """
    import sys, re
    score = sys.maxint
    if not d.get("_PyType") == "Name":
        return sys.maxint
    if re.match("^(B|b)(E|e)(A|a)(M|m)_?(S|s)(E|e)(T|t)$", d.get("id")) != None:
        score = min(score, 0)
    if re.match("(B|b)(E|e)(A|a)(M|m)_?(S|s)(E|e)(T|t).*(?<!s)$", d.get("id")) != None:
        score = min(score, 0)
    return score