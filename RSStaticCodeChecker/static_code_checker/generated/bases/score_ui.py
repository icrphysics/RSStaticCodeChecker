def get_score(d):
    """
    checks the score for a dict representing the AST node for the base entry 'ui'
    """
    import sys, re
    score = sys.maxint
    if not d.get("_PyType") == "Name":
        return sys.maxint
    if re.match("^(U|u)(I|i)$", d.get("id")) != None:
        score = min(score, 0)
    if re.match(".*(U|u)(I|i).*(?<!s)$", d.get("id")) != None:
        score = min(score, 1)
    return score