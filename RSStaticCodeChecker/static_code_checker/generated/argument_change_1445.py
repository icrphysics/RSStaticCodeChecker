import lib.lib as lib
import json
def easyCheck(s):
    return "EditResearchOptimizationFunction" in s
def scoreForDict(d):
    import sys
    if not isinstance(d, dict):
        return sys.maxint
    arguments_right_result = argumentsRight(d)
    if arguments_right_result != True:
        return (float(arguments_right_result) + float(prefixScore(d)))/2.0
    return sys.maxint
def argumentsRight(d):
    args = ["Function","RoiName","Parameters","Weight","IsConstraint","RestrictAllBeamsIndividually","RestrictToBeam","RestrictToBeamSet","UseRbeDose"]
    too_many = []
    for keyword in d.get("keywords", []):
        if keyword.get("arg") in args:
            args.remove(keyword.get("arg"))
        else:
            too_many.append(keyword.get("arg"))
    if not too_many and not args:
        return True
    return (0 if too_many else 3)
def prefixScore(d):
    import sys
    score = sys.maxint
    steps = 0
    if not d.get("_PyType") == "Call":
        return sys.maxint
    _d = d.get("func")
    score = dictMatchScore_0(_d)
    if score != sys.maxint:
        return score
    return sys.maxint
def dictMatchScore_0(d):
    import sys
    score = 0
    steps = 0
    from bases import score_Case
    steps += 1
    score_temp = lib.score_generic(d, "EditResearchOptimizationFunction")
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    steps += 1
    score_temp = lib.score_generic(d.get("value"), "[]")
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    steps += 1
    score_temp = lib.score_generic(d.get("value").get("value"), "PlanOptimizations")
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    steps += 1
    score_temp = lib.score_generic(d.get("value").get("value").get("value"), "[]")
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    steps += 1
    score_temp = lib.score_generic(d.get("value").get("value").get("value").get("value"), "TreatmentPlans")
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    steps += 1
    score_temp = score_Case.get_score(d.get("value").get("value").get("value").get("value").get("value"))
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    return float(score) / float(steps)
def get_info():
    return json.loads("{\"base\": \"Case.TreatmentPlans.[].PlanOptimizations.[]\", \"params\": [\"Function\", \"RoiName\", \"Parameters\", \"Weight\", \"IsConstraint\", \"RestrictAllBeamsIndividually\", \"RestrictToBeam\", \"RestrictToBeamSet\", \"UseRbeDose\"], \"method\": \"EditResearchOptimizationFunction\", \"description\": \"EditResearchOptimizationFunction(..)\\r\\n  Edits a research objective constituent.\\r\\n  Parameters:\\r\\n    Function - The objective constituent that should be edited.\\r\\n    RoiName - Name of the function dependent ROI.\\r\\n    Parameters - String holding the parameters of the research \\r\\n      function.\\r\\n      The first word must be the name of the research function.\\r\\n    Weight - The weight of the objective function.\\r\\n      Not used if the function is a constraint.\\r\\n    IsConstraint - True if the function is a constraint, false \\r\\n      otherwise.\\r\\n    RestrictAllBeamsIndividually - Restricts the function to \\r\\n      all beams individually. Default is false.\\r\\n    RestrictToBeam - Restricts the function to the beam with \\r\\n      the given name.\\r\\n      Null means no restriction. Default is null.\\r\\n    RestrictToBeamSet - Restricts the function to the beam set \\r\\n      with the given name.\\r\\n      Null means that the function operates on the plan dose. \\r\\n      Default is null.\\r\\n    UseRbeDose - True if the function should target RBE dose; \\r\\n      false if it should target physical dose.\\r\\n\"}")
