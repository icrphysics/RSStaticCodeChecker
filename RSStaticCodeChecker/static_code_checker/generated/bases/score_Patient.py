def get_score(d):
    """
    checks the score for a dict representing the AST node for the base entry 'Patient'
    """
    import sys, re
    score = sys.maxint
    if not d.get("_PyType") == "Name":
        return sys.maxint
    if re.match("^(P|p)(A|a)(T|t)(I|i)(E|e)(N|n)(T|t)$", d.get("id")) != None:
        score = min(score, 0)
    if re.match(".*(P|p)(A|a)(T|t)(I|i)(E|e)(N|n)(T|t).*(?<!s)$", d.get("id")) != None:
        score = min(score, 1)
    if re.match("^(P|p)(A|a)(T|t)$", d.get("id")) != None:
        score = min(score, 2)
    if re.match(".*(P|p)(A|a)(T|t).*(?<!s)$", d.get("id")) != None:
        score = min(score, 3)
    return score