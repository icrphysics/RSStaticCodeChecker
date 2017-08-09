import lib.lib as lib
import json
def easyCheck(s):
    return "Create4DCTProjection" in s
def scoreForDict(d):
    import sys
    if not isinstance(d, dict):
        return sys.maxint
    arguments_right_result = argumentsRight(d)
    if arguments_right_result != True:
        return (float(arguments_right_result) + float(prefixScore(d)))/2.0
    return sys.maxint
def argumentsRight(d):
    args = ["ExaminationName","ExaminationGroupName","ProjectionMethod"]
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
    score_temp = lib.score_generic(d, "Create4DCTProjection")
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
    return json.loads("{\"base\": \"Case\", \"params\": [\"ExaminationName\", \"ExaminationGroupName\", \"ProjectionMethod\"], \"method\": \"Create4DCTProjection\", \"description\": \"Create4DCTProjection(..)\\r\\n  Creates a projection of a 4DCT using minimum-, maximum- or \\r\\n  average intensity projection.\\r\\n  Parameters:\\r\\n    ExaminationName - Name of the output examination.\\r\\n    ExaminationGroupName - Name of the input examination group.\\r\\n    ProjectionMethod - The projection method. Possible values:\\r\\n      * MaximumIntensity\\r\\n      * MinimumIntensity\\r\\n      * AverageIntensity\\r\\n\"}")
