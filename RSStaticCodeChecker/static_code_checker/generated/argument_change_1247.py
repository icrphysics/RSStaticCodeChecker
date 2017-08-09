import lib.lib as lib
import json
def easyCheck(s):
    return "GetAccumulatedDeliveredDose" in s
def scoreForDict(d):
    import sys
    if not isinstance(d, dict):
        return sys.maxint
    arguments_right_result = argumentsRight(d)
    if arguments_right_result != True:
        return (float(arguments_right_result) + float(prefixScore(d)))/2.0
    return sys.maxint
def argumentsRight(d):
    args = ["FromFractionNumber","ToFractionNumber"]
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
    score_temp = lib.score_generic(d, "GetAccumulatedDeliveredDose")
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    steps += 1
    score_temp = lib.score_generic(d.get("value"), "TreatmentDelivery")
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    steps += 1
    score_temp = score_Case.get_score(d.get("value").get("value"))
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    return float(score) / float(steps)
def get_info():
    return json.loads("{\"base\": \"Case.TreatmentDelivery\", \"params\": [\"FromFractionNumber\", \"ToFractionNumber\"], \"method\": \"GetAccumulatedDeliveredDose\", \"description\": \"GetAccumulatedDeliveredDose(..)\\r\\n  Gets a dose distribution corresponding to an accumulated \\r\\n  delivered dose\\r\\n  Can only be used for Patient.TreatmentDelivery.TreatmentCourse (an \\r\\n  exception is thrown if applied to TreatmentCourse under \\r\\n  TreatmentPlan)\\r\\n  TreatmentFractions need to have \\r\\n  EstimatedDoseOnTotalDoseExamination calculated consecutivly \\r\\n  between FromFractionNumber and ToFractionNumber\\r\\n              \\r\\n  Experimental - use with care\\r\\n  Parameters:\\r\\n    FromFractionNumber - The fraction number you want to start \\r\\n      accumulating from (needs to be 1 or larger)\\r\\n    ToFractionNumber - The fraction number you want to start \\r\\n      accumulating to\\r\\n  Returns:\\r\\n    DoseDistribution with accumulated delivered dose\\r\\n\"}")
