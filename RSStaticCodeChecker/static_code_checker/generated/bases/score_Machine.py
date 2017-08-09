def get_score(d):
    """
    checks the score for a dict representing the AST node for the base entry 'Machine'
    """
    import sys, re
    score = sys.maxint
    if not d.get("_PyType") == "Name":
        return sys.maxint
    if re.match("^(M|m)(A|a)(C|c)(H|h)(I|i)(N|n)(E|e)(?<!s)$", d.get("id")) != None:
        score = min(score, 0)
    if re.match("(M|m)(A|a)(C|c)(H|h)(I|i)(N|n)(E|e).*(?<!s)$", d.get("id")) != None:
        score = min(score, 1)
    return score