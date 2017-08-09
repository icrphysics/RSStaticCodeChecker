def get_score(d):
    """
    checks the score for a dict representing the AST node for the base entry 'Examination'
    """
    import sys, re
    score = sys.maxint
    if not d.get("_PyType") == "Name":
        return sys.maxint
    if re.match("^(E|e)(X|x)(A|a)(M|m)(I|i)(N|n)(A|a)(T|t)(I|i)(O|o)(N|n)$", d.get("id")) != None:
        score = min(score, 0)
    if re.match(".*(E|e)(X|x)(A|a)(M|m)(I|i)(N|n)(A|a)(T|t)(I|i)(O|o)(N|n).*(?<!s)$", d.get("id")) != None:
        score = min(score, 1)
    if re.match("^(E|e)(X|x)(A|a)(M|m)$", d.get("id")) != None:
        score = min(score, 2)
    if re.match(".*(E|e)(X|x)(A|a)(M|m).*(?<!s)$", d.get("id")) != None:
        score = min(score, 3)
    return score