import lib.lib as lib
import json
def easyCheck(s):
    return "EditOptimizationFunction" in s
def scoreForDict(d):
    import sys
    if not isinstance(d, dict):
        return sys.maxint
    arguments_right_result = argumentsRight(d)
    if arguments_right_result != True:
        return (float(arguments_right_result) + float(prefixScore(d)))/2.0
    return sys.maxint
def argumentsRight(d):
    args = ["FunctionType","DoseBasedRoiFunction","RoiName","IsConstraint","RestrictAllBeamsIndividually","RestrictToBeam","IsRobust","RestrictToBeamSet","UseRbeDose"]
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
    from bases import score_Patient
    steps += 1
    score_temp = lib.score_generic(d, "EditOptimizationFunction")
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
    score_temp = lib.score_generic(d.get("value").get("value").get("value").get("value").get("value"), "[]")
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    steps += 1
    score_temp = lib.score_generic(d.get("value").get("value").get("value").get("value").get("value").get("value"), "Cases")
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    steps += 1
    score_temp = score_Patient.get_score(d.get("value").get("value").get("value").get("value").get("value").get("value").get("value"))
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    return float(score) / float(steps)
def get_info():
    return json.loads("{\"base\": \"Patient.Cases.[].TreatmentPlans.[].PlanOptimizations.[]\", \"params\": [\"FunctionType\", \"DoseBasedRoiFunction\", \"RoiName\", \"IsConstraint\", \"RestrictAllBeamsIndividually\", \"RestrictToBeam\", \"IsRobust\", \"RestrictToBeamSet\", \"UseRbeDose\"], \"method\": \"EditOptimizationFunction\", \"description\": \"EditOptimizationFunction(..)\\r\\n  Edits an objective constituent or a constraint.\\r\\n  Parameters:\\r\\n    FunctionType - The function type.\\r\\n      * MinDose\\r\\n      * MaxDose\\r\\n      * MinDvh \\r\\n      * MaxDvh\\r\\n      * UniformDose \\r\\n      * MinEud \\r\\n      * MaxEud\\r\\n      * TargetEud\\r\\n      * DoseFallOff\\r\\n      * UniformityConstraint\\r\\n    DoseBasedRoiFunction - The objective constituent or a \\r\\n      constraint that should be edited.\\r\\n    RoiName - Name of the function dependent ROI.\\r\\n    IsConstraint - Whether the function is to be a constraint \\r\\n      or an objective.\\r\\n    RestrictAllBeamsIndividually - If the restriction is to be \\r\\n      applied to all beams individually. Only used for Protons or \\r\\n      physical Carbon dose.\\r\\n    RestrictToBeam - Name of the beam when restricting dose \\r\\n      dependencies to a single beam.\\r\\n      Null means no restriction. Only used for Protons or physical \\r\\n      Carbon dose.\\r\\n    IsRobust - Whether the worst-case robustness should be \\r\\n      used (requieres parameters in robustness settings).\\r\\n    RestrictToBeamSet - Whether the function should refer to \\r\\n      total dose or beam set dose.\\r\\n    UseRbeDose - True if the function should target RBE dose; \\r\\n      false if it should target physical dose.\\r\\n      Not used for modalities not using RBE dose (i.e. Photons, \\r\\n      Electrons and Protons).\\r\\n\"}")
