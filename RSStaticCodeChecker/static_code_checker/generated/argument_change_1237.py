import lib.lib as lib
import json
def easyCheck(s):
    return "CreateDefaultVSimPlan" in s
def scoreForDict(d):
    import sys
    if not isinstance(d, dict):
        return sys.maxint
    arguments_right_result = argumentsRight(d)
    if arguments_right_result != True:
        return (float(arguments_right_result) + float(prefixScore(d)))/2.0
    return sys.maxint
def argumentsRight(d):
    args = ["Isocenter","ExaminationName"]
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
    score_temp = lib.score_generic(d, "CreateDefaultVSimPlan")
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
    return json.loads("{\"base\": \"Case\", \"params\": [\"Isocenter\", \"ExaminationName\"], \"method\": \"CreateDefaultVSimPlan\", \"description\": \"CreateDefaultVSimPlan(..)\\r\\n  Adds a new treatment plan using the default machine specified in \\r\\n  ClinicDB. If the machine\\r\\n  is not found, the first commissioned, non deprecated linac machine \\r\\n  in alpabethical order is used.\\r\\n  Example:\\r\\n    To create a plan: \\r\\n    case.CreateDefaultVSimPlan(Isocenter={ 'x': 0.0, 'y': 0.0, 'z': \\r\\n    0.0 },ExaminationName=\\\"CT 1\\\")\\r\\n  Parameters:\\r\\n    Isocenter - Coordinates of isocenter\\r\\n    ExaminationName - The name of the examination on which the \\r\\n      dose grid is defined.\\r\\n  Returns:\\r\\n    Warning message, if any.\\r\\n\"}")
