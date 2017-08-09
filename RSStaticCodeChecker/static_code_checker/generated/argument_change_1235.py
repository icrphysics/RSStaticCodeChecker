import lib.lib as lib
import json
def easyCheck(s):
    return "MapDose" in s
def scoreForDict(d):
    import sys
    if not isinstance(d, dict):
        return sys.maxint
    arguments_right_result = argumentsRight(d)
    if arguments_right_result != True:
        return (float(arguments_right_result) + float(prefixScore(d)))/2.0
    return sys.maxint
def argumentsRight(d):
    args = ["FractionNumber","SetTotalDoseEstimateReference","DoseDistribution","StructureRegistration"]
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
    score_temp = lib.score_generic(d, "MapDose")
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
    return json.loads("{\"base\": \"Case\", \"params\": [\"FractionNumber\", \"SetTotalDoseEstimateReference\", \"DoseDistribution\", \"StructureRegistration\"], \"method\": \"MapDose\", \"description\": \"MapDose(..)\\r\\n  Action for mapping dose from the target examination of the \\r\\n  registration to the reference examination of the registration.\\r\\n  Note that it is possible to map a dose that has already been \\r\\n  mapped with the same registration.\\r\\n  This will create two evaluation doses with the same properties.\\r\\n  Parameters:\\r\\n    FractionNumber - The fraction number of the dose \\r\\n      distribution.\\r\\n      Default is zero.\\r\\n    SetTotalDoseEstimateReference - Indicates if total dose \\r\\n      estimate reference should be set.\\r\\n      Default is false.\\r\\n    DoseDistribution - The dose distribution to map.\\r\\n    StructureRegistration - The deformable registration to be \\r\\n      used for the dose mapping.\\r\\n      The dose distribution must be defined on the target \\r\\n      examination of this registration.\\r\\n\"}")
