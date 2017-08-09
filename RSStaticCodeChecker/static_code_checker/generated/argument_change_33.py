import lib.lib as lib
import json
def easyCheck(s):
    return "SetWeightedDose" in s
def scoreForDict(d):
    import sys
    if not isinstance(d, dict):
        return sys.maxint
    arguments_right_result = argumentsRight(d)
    if arguments_right_result != True:
        return (float(arguments_right_result) + float(prefixScore(d)))/2.0
    return sys.maxint
def argumentsRight(d):
    args = ["PlanNames","Weights"]
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
    score_temp = lib.score_generic(d, "SetWeightedDose")
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    steps += 1
    score_temp = lib.score_generic(d.get("value"), "TotalDose")
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    steps += 1
    score_temp = lib.score_generic(d.get("value").get("value"), "TreatmentCourse")
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    steps += 1
    score_temp = lib.score_generic(d.get("value").get("value").get("value"), "TreatmentDelivery")
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    steps += 1
    score_temp = lib.score_generic(d.get("value").get("value").get("value").get("value"), "[]")
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    steps += 1
    score_temp = lib.score_generic(d.get("value").get("value").get("value").get("value").get("value"), "Cases")
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    steps += 1
    score_temp = score_Patient.get_score(d.get("value").get("value").get("value").get("value").get("value").get("value"))
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    return float(score) / float(steps)
def get_info():
    return json.loads("{\"base\": \"Patient.Cases.[].TreatmentDelivery.TreatmentCourse.TotalDose\", \"params\": [\"PlanNames\", \"Weights\"], \"method\": \"SetWeightedDose\", \"description\": \"SetWeightedDose(..)\\r\\n  Sets the dose to a weighted sum of the \\r\\n  fraction doses of the beam sets for a number of plans.\\r\\n  If the dose distribution is a fraction dose, the plan dose is \\r\\n  updated accordingly.\\r\\n  An exception is thrown if the dose distribution is a composite \\r\\n  dose, if the PlanNames array \\r\\n  is longer than the Weights array, if the PlanNames array contains \\r\\n  a name that does not \\r\\n  match any plan name for the current patient, if any of the plans \\r\\n  in the PlanNames array \\r\\n  contains no beam set or more than one beam set or if any of the \\r\\n  plans in the PlanNames array \\r\\n  does not have a computed fraction dose.\\r\\n  Parameters:\\r\\n    PlanNames - A list of the names of the plans whose \\r\\n      fraction doses will be used for the dose sum.\\r\\n    Weights - A list of the weights of the fraction doses.\\r\\n\"}")
