import lib.lib as lib
import json
def easyCheck(s):
    return "SaveRobustnessParameters" in s
def scoreForDict(d):
    import sys
    if not isinstance(d, dict):
        return sys.maxint
    arguments_right_result = argumentsRight(d)
    if arguments_right_result != True:
        return (float(arguments_right_result) + float(prefixScore(d)))/2.0
    return sys.maxint
def argumentsRight(d):
    args = ["PositionUncertaintyAnterior","PositionUncertaintyPosterior","PositionUncertaintySuperior","PositionUncertaintyInferior","PositionUncertaintyLeft","PositionUncertaintyRight","DensityUncertainty","IndependentBeams","ComputeExactScenarioDoses","NamesOfNonPlanningExaminations"]
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
    score_temp = lib.score_generic(d, "SaveRobustnessParameters")
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    steps += 1
    score_temp = lib.score_generic(d.get("value"), "OptimizationParameters")
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    steps += 1
    score_temp = lib.score_generic(d.get("value").get("value"), "[]")
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    steps += 1
    score_temp = lib.score_generic(d.get("value").get("value").get("value"), "PlanOptimizations")
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    steps += 1
    score_temp = score_Plan.get_score(d.get("value").get("value").get("value").get("value"))
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    return float(score) / float(steps)
def get_info():
    return json.loads("{\"base\": \"Plan.PlanOptimizations.[].OptimizationParameters\", \"params\": [\"PositionUncertaintyAnterior\", \"PositionUncertaintyPosterior\", \"PositionUncertaintySuperior\", \"PositionUncertaintyInferior\", \"PositionUncertaintyLeft\", \"PositionUncertaintyRight\", \"DensityUncertainty\", \"IndependentBeams\", \"ComputeExactScenarioDoses\", \"NamesOfNonPlanningExaminations\"], \"method\": \"SaveRobustnessParameters\", \"description\": \"SaveRobustnessParameters(..)\\r\\n  Saves robustness parameters.\\r\\n  Parameters:\\r\\n    PositionUncertaintyAnterior - The \\r\\n      PositionUncertaintyAnterior that shall be copied.\\r\\n    PositionUncertaintyPosterior - The \\r\\n      PositionUncertaintyPosterior that shall be copied.\\r\\n    PositionUncertaintySuperior - The \\r\\n      PositionUncertaintySuperior that shall be copied.\\r\\n    PositionUncertaintyInferior - The \\r\\n      PositionUncertaintyInferior that shall be copied.\\r\\n    PositionUncertaintyLeft - The PositionUncertaintyLeft that \\r\\n      shall be copied.\\r\\n    PositionUncertaintyRight - The PositionUncertaintyRight \\r\\n      that shall be copied.\\r\\n    DensityUncertainty - The DensityUncertainty that shall be \\r\\n      copied.\\r\\n    IndependentBeams - The IndependentBeams that shall be \\r\\n      copied.\\r\\n    ComputeExactScenarioDoses - The ComputeExactScenarioDoses \\r\\n      that shall be copied.\\r\\n    NamesOfNonPlanningExaminations - Examinations that shall \\r\\n      be considered, disregarding the planning examination.\\r\\n\"}")
