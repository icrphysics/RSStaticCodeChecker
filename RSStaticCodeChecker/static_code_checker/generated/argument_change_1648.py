import lib.lib as lib
import json
def easyCheck(s):
    return "CopyPlanAndAddAsNewBeamSet" in s
def scoreForDict(d):
    import sys
    if not isinstance(d, dict):
        return sys.maxint
    arguments_right_result = argumentsRight(d)
    if arguments_right_result != True:
        return (float(arguments_right_result) + float(prefixScore(d)))/2.0
    return sys.maxint
def argumentsRight(d):
    args = ["PlanName","NewBeamSetName"]
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
    score_temp = lib.score_generic(d, "CopyPlanAndAddAsNewBeamSet")
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
    score_temp = lib.score_generic(d.get("value").get("value"), "TreatmentPlans")
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    steps += 1
    score_temp = score_Case.get_score(d.get("value").get("value").get("value"))
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    return float(score) / float(steps)
def get_info():
    return json.loads("{\"base\": \"Case.TreatmentPlans.[]\", \"params\": [\"PlanName\", \"NewBeamSetName\"], \"method\": \"CopyPlanAndAddAsNewBeamSet\", \"description\": \"CopyPlanAndAddAsNewBeamSet(..)\\r\\n  Copies a plan (with one beam set) and adds it as new beam set to \\r\\n  another plan.\\r\\n  The same prerequisites as when adding a new beam set to the \\r\\n  current plan, i.e.,\\r\\n   - same planning image\\r\\n   - same patient position\\r\\n   - same dose grid size, corner and resolution\\r\\n   - supported delivery technique\\r\\n   - commissioned machine\\r\\n              \\r\\n  A deep clone of the radiation set is done. Objective functions are \\r\\n  not copied over.\\r\\n  Parameters:\\r\\n    PlanName - Name of the plan to copy.\\r\\n    NewBeamSetName - The name of the new beam set.\\r\\n\"}")
