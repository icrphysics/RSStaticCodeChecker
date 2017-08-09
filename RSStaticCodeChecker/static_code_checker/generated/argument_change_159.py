import lib.lib as lib
import json
def easyCheck(s):
    return "CreateBreastPlan" in s
def scoreForDict(d):
    import sys
    if not isinstance(d, dict):
        return sys.maxint
    arguments_right_result = argumentsRight(d)
    if arguments_right_result != True:
        return (float(arguments_right_result) + float(prefixScore(d)))/2.0
    return sys.maxint
def argumentsRight(d):
    args = ["PlanName","Examination","PlannedBy","DoseGridResolution","NumberOfFractions","TreatmentMachine","CreateSetupBeams","UniformDoseToTarget","TargetName","TargetColor"]
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
    score_temp = lib.score_generic(d, "CreateBreastPlan")
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
    score_temp = lib.score_generic(d.get("value").get("value"), "Cases")
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    steps += 1
    score_temp = score_Patient.get_score(d.get("value").get("value").get("value"))
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    return float(score) / float(steps)
def get_info():
    return json.loads("{\"base\": \"Patient.Cases.[]\", \"params\": [\"PlanName\", \"Examination\", \"PlannedBy\", \"DoseGridResolution\", \"NumberOfFractions\", \"TreatmentMachine\", \"CreateSetupBeams\", \"UniformDoseToTarget\", \"TargetName\", \"TargetColor\"], \"method\": \"CreateBreastPlan\", \"description\": \"CreateBreastPlan(..)\\r\\n  For auto breast planning only.\\r\\n  Creates plan and beam set, sets up prescription, creates dose grid\\r\\n  Parameters:\\r\\n    PlanName - Name of the new plan.\\r\\n    Examination - Name of the examination set to be used.\\r\\n    PlannedBy - Planned by\\r\\n    DoseGridResolution - Dose grid resolution.\\r\\n    NumberOfFractions - Number of fractions.\\r\\n    TreatmentMachine - Name of the Treatment machine.\\r\\n    CreateSetupBeams - Create setup beams.\\r\\n    UniformDoseToTarget - Prescription in cGy to CTV.\\r\\n    TargetName - Name of the target ROI ('aCTV').\\r\\n    TargetColor - Color of the target ROI.\\r\\n\"}")
