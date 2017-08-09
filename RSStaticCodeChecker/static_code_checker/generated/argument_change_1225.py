import lib.lib as lib
import json
def easyCheck(s):
    return "SetRegistrationAsTreatmentPositionAlignment" in s
def scoreForDict(d):
    import sys
    if not isinstance(d, dict):
        return sys.maxint
    arguments_right_result = argumentsRight(d)
    if arguments_right_result != True:
        return (float(arguments_right_result) + float(prefixScore(d)))/2.0
    return sys.maxint
def argumentsRight(d):
    args = ["FractionExamination","PlanningExamination"]
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
    score_temp = lib.score_generic(d, "SetRegistrationAsTreatmentPositionAlignment")
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    steps += 1
    score_temp = score_Case.get_score(d.get("value"))
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    return float(score) / float(steps)
def get_info():
    return json.loads("{\"base\": \"Case\", \"params\": [\"FractionExamination\", \"PlanningExamination\"], \"method\": \"SetRegistrationAsTreatmentPositionAlignment\", \"description\": \"SetRegistrationAsTreatmentPositionAlignment(..)\\r\\n  Sets a frame-of reference registration as treatment position \\r\\n  alignment.\\r\\n  To be able to use this functionality a frame-of-reference \\r\\n  registration with the fraction image set as floating image set and \\r\\n  the the planning image set as reference image set has to exist.\\r\\n  Note: A treatment position alignment corresponds to the \\r\\n  relationship between the planning image set and the actual \\r\\n  treatment position during the fraction.\\r\\n  Hence, only set a frame-of-reference registration corresponding to \\r\\n  the relationship between the planning image set and the actual \\r\\n  treatment position as being treatment position alignment.\\r\\n  Parameters:\\r\\n    FractionExamination - The image set acquired during \\r\\n      treatment.\\r\\n      This image set needs to be assigned to a fraction.\\r\\n    PlanningExamination - The planning image set of the plan \\r\\n      for which treatment adaptation has been initialized.\\r\\n\"}")
