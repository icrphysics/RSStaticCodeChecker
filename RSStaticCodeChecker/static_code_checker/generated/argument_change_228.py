import lib.lib as lib
import json
def easyCheck(s):
    return "EditBeamOptimizationSettings" in s
def scoreForDict(d):
    import sys
    if not isinstance(d, dict):
        return sys.maxint
    arguments_right_result = argumentsRight(d)
    if arguments_right_result != True:
        return (float(arguments_right_result) + float(prefixScore(d)))/2.0
    return sys.maxint
def argumentsRight(d):
    args = ["OptimizationTypes","SelectCollimatorAngle","AllowBeamSplit","JawMotion","LeftJaw","RightJaw","TopJaw","BottomJaw"]
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
    score_temp = lib.score_generic(d, "EditBeamOptimizationSettings")
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
    score_temp = lib.score_generic(d.get("value").get("value"), "BeamSettings")
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
    score_temp = lib.score_generic(d.get("value").get("value").get("value").get("value"), "TreatmentSetupSettings")
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    steps += 1
    score_temp = lib.score_generic(d.get("value").get("value").get("value").get("value").get("value"), "OptimizationParameters")
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    steps += 1
    score_temp = lib.score_generic(d.get("value").get("value").get("value").get("value").get("value").get("value"), "[]")
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    steps += 1
    score_temp = lib.score_generic(d.get("value").get("value").get("value").get("value").get("value").get("value").get("value"), "PlanOptimizations")
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    steps += 1
    score_temp = lib.score_generic(d.get("value").get("value").get("value").get("value").get("value").get("value").get("value").get("value"), "[]")
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    steps += 1
    score_temp = lib.score_generic(d.get("value").get("value").get("value").get("value").get("value").get("value").get("value").get("value").get("value"), "TreatmentPlans")
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    steps += 1
    score_temp = lib.score_generic(d.get("value").get("value").get("value").get("value").get("value").get("value").get("value").get("value").get("value").get("value"), "[]")
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    steps += 1
    score_temp = lib.score_generic(d.get("value").get("value").get("value").get("value").get("value").get("value").get("value").get("value").get("value").get("value").get("value"), "Cases")
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    steps += 1
    score_temp = score_Patient.get_score(d.get("value").get("value").get("value").get("value").get("value").get("value").get("value").get("value").get("value").get("value").get("value").get("value"))
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    return float(score) / float(steps)
def get_info():
    return json.loads("{\"base\": \"Patient.Cases.[].TreatmentPlans.[].PlanOptimizations.[].OptimizationParameters.TreatmentSetupSettings.[].BeamSettings.[]\", \"params\": [\"OptimizationTypes\", \"SelectCollimatorAngle\", \"AllowBeamSplit\", \"JawMotion\", \"LeftJaw\", \"RightJaw\", \"TopJaw\", \"BottomJaw\"], \"method\": \"EditBeamOptimizationSettings\", \"description\": \"EditBeamOptimizationSettings(..)\\r\\n  Edits the beam optimization settings for selected beam\\r\\n  Parameters:\\r\\n    OptimizationTypes - Enumerator describing how a beam may \\r\\n      be optimized.\\r\\n      That is, in which manner the optimization should be performed.\\r\\n      The enumerator array is a combination of different allowed \\r\\n      optimizations.\\r\\n    SelectCollimatorAngle - If true, select collimator angle \\r\\n      at sequencing.\\r\\n    AllowBeamSplit - Indicates if a beam split should be \\r\\n      attempted when the field is to wide for current machine \\r\\n      contraints.\\r\\n    JawMotion - Can be any of the following strings:\\r\\n      \\\"Fixed\\\"\\r\\n      \\\"Automatic\\\"\\r\\n      \\\"Lock to limits\\\"\\r\\n      \\\"Use limits as max\\\"\\r\\n    LeftJaw - Left jaw [X1].\\r\\n    RightJaw - Right jaw [X2].\\r\\n    TopJaw - Top jaw [Y1].\\r\\n    BottomJaw - Bottom jaw [Y2].\\r\\n\"}")
