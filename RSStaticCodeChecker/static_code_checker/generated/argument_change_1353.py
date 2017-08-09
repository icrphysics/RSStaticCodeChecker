import lib.lib as lib
import json
def easyCheck(s):
    return "SumTwoDoses" in s
def scoreForDict(d):
    import sys
    if not isinstance(d, dict):
        return sys.maxint
    arguments_right_result = argumentsRight(d)
    if arguments_right_result != True:
        return (float(arguments_right_result) + float(prefixScore(d)))/2.0
    return sys.maxint
def argumentsRight(d):
    args = ["Dose1","Dose2","Weight1","Weight2","DoseName"]
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
    score_temp = lib.score_generic(d, "SumTwoDoses")
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
    return json.loads("{\"base\": \"Case\", \"params\": [\"Dose1\", \"Dose2\", \"Weight1\", \"Weight2\", \"DoseName\"], \"method\": \"SumTwoDoses\", \"description\": \"SumTwoDoses(..)\\r\\n  Sums two dose distributions.\\r\\n  Parameters:\\r\\n    Dose1 - The first dose distribution.\\r\\n    Dose2 - The second dose distribution.\\r\\n    Weight1 - The weight of the first dose distribution. Must \\r\\n      be a positive number.\\r\\n    Weight2 - The weight of the second dose distribution. Must \\r\\n      be a positive number.\\r\\n    DoseName - The name of the summed dose. Cannot be empty.\\r\\n\"}")
