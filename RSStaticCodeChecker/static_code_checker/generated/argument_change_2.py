import lib.lib as lib
import json
def easyCheck(s):
    return "CalculateGammaForFractionDose" in s
def scoreForDict(d):
    import sys
    if not isinstance(d, dict):
        return sys.maxint
    arguments_right_result = argumentsRight(d)
    if arguments_right_result != True:
        return (float(arguments_right_result) + float(prefixScore(d)))/2.0
    return sys.maxint
def argumentsRight(d):
    args = ["EvaluationPlan","ReferencePlan","DistanceCriteria","DoseCriteria","SampleDistance","NumberOfRefineIterations","RefineLayers","Limit"]
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
    score_temp = lib.score_generic(d, "CalculateGammaForFractionDose")
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    steps += 1
    score_temp = score_Patient.get_score(d.get("value"))
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    return float(score) / float(steps)
def get_info():
    return json.loads("{\"base\": \"Patient\", \"params\": [\"EvaluationPlan\", \"ReferencePlan\", \"DistanceCriteria\", \"DoseCriteria\", \"SampleDistance\", \"NumberOfRefineIterations\", \"RefineLayers\", \"Limit\"], \"method\": \"CalculateGammaForFractionDose\", \"description\": \"CalculateGammaForFractionDose(..)\\r\\n  Method to calculate gamma using global maximum dose. It can be \\r\\n  used for cases when the dose grid of the evaluated plan is the \\r\\n  same as for the reference plan. \\r\\n  The method requires that for each plan there is only one study, \\r\\n  one treatment case, one treatment plan group and one beam set. \\r\\n  Gamma is calculated using the fraction dose. \\r\\n  This method is for experimental use - use with care.\\r\\n  Parameters:\\r\\n    EvaluationPlan - The name of the evaluated plan.\\r\\n    ReferencePlan - The name of the reference plan.\\r\\n    DistanceCriteria - Distance criteria in cm for the gamma \\r\\n      evaluation.\\r\\n    DoseCriteria - Dose criteria in percent for the gamma \\r\\n      evaluation.\\r\\n    SampleDistance - Distance between points that will be \\r\\n      evaluated by the gamma algorithm [cm].\\r\\n    NumberOfRefineIterations - Number of refined searches for \\r\\n      an optimal gamma value.\\r\\n    RefineLayers - Affects the distance that will be searched \\r\\n      for an optimal gamma value.\\r\\n    Limit - The maximum gamma value calculated, higher values \\r\\n      will be truncated.\\r\\n  Returns:\\r\\n    The gamma distribution.\\r\\n\"}")
