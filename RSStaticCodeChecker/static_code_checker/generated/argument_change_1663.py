import lib.lib as lib
import json
def easyCheck(s):
    return "SetImagingSystemReference" in s
def scoreForDict(d):
    import sys
    if not isinstance(d, dict):
        return sys.maxint
    arguments_right_result = argumentsRight(d)
    if arguments_right_result != True:
        return (float(arguments_right_result) + float(prefixScore(d)))/2.0
    return sys.maxint
def argumentsRight(d):
    args = ["ImagingSystemName"]
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
    from bases import score_Examination
    steps += 1
    score_temp = lib.score_generic(d, "SetImagingSystemReference")
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    steps += 1
    score_temp = lib.score_generic(d.get("value"), "EquipmentInfo")
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    steps += 1
    score_temp = score_Examination.get_score(d.get("value").get("value"))
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    return float(score) / float(steps)
def get_info():
    return json.loads("{\"base\": \"Examination.EquipmentInfo\", \"params\": [\"ImagingSystemName\"], \"method\": \"SetImagingSystemReference\", \"description\": \"SetImagingSystemReference(..)\\r\\n  Action that sets ImagingSystemReference for the EquipmentInfo of \\r\\n  an Examination. \\r\\n  If the examination belongs to an 4DCT group, all examinations in \\r\\n  the group will be assigned the selected ImagingSystem.\\r\\n  Only commissioned, nondepricated ImagingSystems can be used.\\r\\n  If the selected ImagingSystem is a CBCT machine, Modality will be \\r\\n  updated to 'CBCT'.\\r\\n  Parameters:\\r\\n    ImagingSystemName - The name of the ImagingSystem\\r\\n      Note: if left empty ImagingSystem will be assigned 'None'. If \\r\\n      changing from a CBCT machine, Modality will be updated to 'CT'\\r\\n\"}")
