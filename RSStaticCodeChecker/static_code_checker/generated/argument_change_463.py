import lib.lib as lib
import json
def easyCheck(s):
    return "AddClinicalGoal" in s
def scoreForDict(d):
    import sys
    if not isinstance(d, dict):
        return sys.maxint
    arguments_right_result = argumentsRight(d)
    if arguments_right_result != True:
        return (float(arguments_right_result) + float(prefixScore(d)))/2.0
    return sys.maxint
def argumentsRight(d):
    args = ["RoiName","GoalCriteria","GoalType","AcceptanceLevel","ParameterValue","IsComparativeGoal","Priority"]
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
    from bases import score_Plan
    steps += 1
    score_temp = lib.score_generic(d, "AddClinicalGoal")
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    steps += 1
    score_temp = lib.score_generic(d.get("value"), "EvaluationSetup")
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    steps += 1
    score_temp = lib.score_generic(d.get("value").get("value"), "TreatmentCourseSource")
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
    score_temp = lib.score_generic(d.get("value").get("value").get("value").get("value"), "PlanOptimizations")
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    steps += 1
    score_temp = score_Plan.get_score(d.get("value").get("value").get("value").get("value").get("value"))
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    return float(score) / float(steps)
def get_info():
    return json.loads("{\"base\": \"Plan.PlanOptimizations.[].TreatmentCourseSource.EvaluationSetup\", \"params\": [\"RoiName\", \"GoalCriteria\", \"GoalType\", \"AcceptanceLevel\", \"ParameterValue\", \"IsComparativeGoal\", \"Priority\"], \"method\": \"AddClinicalGoal\", \"description\": \"AddClinicalGoal(..)\\r\\n  Adds a clinical goal to an evaluation setup\\r\\n  Parameters:\\r\\n    RoiName - The name of the ROI or POI the planning goal \\r\\n      shall be evaluated on.\\r\\n    GoalCriteria - The planning goal criteria. Specifies the \\r\\n      region for pass and fail.\\r\\n      * AtLeast: At least criteria.\\r\\n      * AtMost: At most criteria.\\r\\n    GoalType - The planning goal type. \\r\\n      * AverageDose: For comparison with the average dose.\\r\\n      * VolumeAtDose: For comparison of the volume at a specified \\r\\n      dose.\\r\\n      * DoseAtVolume: For comparison of the dose at a specified \\r\\n      volume.\\r\\n      * DoseAtPoint: For comparison with the dose at a certain point.\\r\\n      * AbsoluteVolumeAtDose: For comparison of the absolute volume \\r\\n      at a specified dose.\\r\\n      * DoseAtAbsoluteVolume: For comparison of the dose at a \\r\\n      specified absolute volume.\\r\\n    AcceptanceLevel - The acceptance level. Sets the level for \\r\\n      pass or fail.\\r\\n    ParameterValue - The parameter value. Goal type specific \\r\\n      parameter.\\r\\n    IsComparativeGoal - Determines if the goal is used as a \\r\\n      comparative goal.\\r\\n    Priority - The priority of the clinical goal.\\r\\n\"}")
