def get_score(d):
    """
    checks the score for a dict representing the AST node for the base entry 'PatientDB'
    """
    import sys, re
    score = sys.maxint
    if not d.get("_PyType") == "Name":
        return sys.maxint
    if re.match("$(P|p)(A|a)(T|t)(I|i)(E|e)(N|n)(T|t)_?(D|d)(B|b)(?<!s)$", d.get("id")) != None:
        score = min(score, 0)
    if re.match(".*(P|p)(A|a)(T|t)(I|i)(E|e)(N|n)(T|t)_?(D|d)(B|b).*(?<!s)$", d.get("id")) != None:
        score = min(score, 1)
    return score