import lib.lib as lib
import json
def easyCheck(s):
    return "SetCtToDensityTableForCbctImage" in s
def scoreForDict(d):
    import sys
    if not isinstance(d, dict):
        return sys.maxint
    arguments_right_result = argumentsRight(d)
    if arguments_right_result != True:
        return (float(arguments_right_result) + float(prefixScore(d)))/2.0
    return sys.maxint
def argumentsRight(d):
    args = ["DensityThresholds"]
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
    score_temp = lib.score_generic(d, "SetCtToDensityTableForCbctImage")
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
    return json.loads("{\"base\": \"Examination.EquipmentInfo\", \"params\": [\"DensityThresholds\"], \"method\": \"SetCtToDensityTableForCbctImage\", \"description\": \"SetCtToDensityTableForCbctImage(..)\\r\\n  Action that sets CtToDensityTable for a CBCT image. In parameter \\r\\n  is an array with five short ints that correspond to the density \\r\\n  thresholds between:\\r\\n    Air to Lung\\r\\n    Lung to Adipose\\r\\n    Adipose to Tissue\\r\\n    Tissue to Cartilage/Bone\\r\\n    Cartilage/Bone to Other\\r\\n  Values within the threshold ranges will be mapped to the following \\r\\n  densities:\\r\\n    Materials.Air             0.00121\\r\\n    Materials.Lung            0.26\\r\\n    Materials.Adipose         0.95\\r\\n    Materials.Tissue          1.05\\r\\n    Materials.CartilageBone   1.6\\r\\n    Materials.Other           3.0\\r\\n  Parameters:\\r\\n    DensityThresholds -  Density thresholds (in CBCT values) \\r\\n      used to create the CT to density table\\r\\n\"}")
