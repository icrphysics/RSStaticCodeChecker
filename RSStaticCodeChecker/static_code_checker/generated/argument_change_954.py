import lib.lib as lib
import json
def easyCheck(s):
    return "GrayLevelThreshold" in s
def scoreForDict(d):
    import sys
    if not isinstance(d, dict):
        return sys.maxint
    arguments_right_result = argumentsRight(d)
    if arguments_right_result != True:
        return (float(arguments_right_result) + float(prefixScore(d)))/2.0
    return sys.maxint
def argumentsRight(d):
    args = ["Examination","LowThreshold","HighThreshold","PetUnit","BoundingBox"]
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
    from bases import score_BeamSet
    steps += 1
    score_temp = lib.score_generic(d, "GrayLevelThreshold")
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    steps += 1
    score_temp = lib.score_generic(d.get("value"), "OfRoi")
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    steps += 1
    score_temp = lib.score_generic(d.get("value").get("value"), "OutlineGeometry")
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    steps += 1
    score_temp = lib.score_generic(d.get("value").get("value").get("value"), "OnDensity")
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    steps += 1
    score_temp = lib.score_generic(d.get("value").get("value").get("value").get("value"), "[]")
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    steps += 1
    score_temp = lib.score_generic(d.get("value").get("value").get("value").get("value").get("value"), "BeamDoses")
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    steps += 1
    score_temp = lib.score_generic(d.get("value").get("value").get("value").get("value").get("value").get("value"), "FractionDose")
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    steps += 1
    score_temp = lib.score_generic(d.get("value").get("value").get("value").get("value").get("value").get("value").get("value"), "BeamListSource")
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
    score_temp = lib.score_generic(d.get("value").get("value").get("value").get("value").get("value").get("value").get("value").get("value").get("value"), "DrrSettings")
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    steps += 1
    score_temp = score_BeamSet.get_score(d.get("value").get("value").get("value").get("value").get("value").get("value").get("value").get("value").get("value").get("value"))
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    return float(score) / float(steps)
def get_info():
    return json.loads("{\"base\": \"BeamSet.DrrSettings.[].BeamListSource.FractionDose.BeamDoses.[].OnDensity.OutlineGeometry.OfRoi\", \"params\": [\"Examination\", \"LowThreshold\", \"HighThreshold\", \"PetUnit\", \"BoundingBox\"], \"method\": \"GrayLevelThreshold\", \"description\": \"GrayLevelThreshold(..)\\r\\n  Gray level thresholding.\\r\\n  Parameters:\\r\\n    Examination - The examination.\\r\\n    LowThreshold - The low threshold. The unit is in rescaled \\r\\n      pixel values, e.g. HU for CT. For PET images, PetUnit must be \\r\\n      specified.\\r\\n    HighThreshold - The high threshold. The unit is in \\r\\n      rescaled pixel values, e.g., HU for CT. For PET images, \\r\\n      PetUnit must be specified.\\r\\n    PetUnit - The unit for PET images. Common values:\\r\\n      * Bq/ml (activity concentration)\\r\\n      * g/ml (SUV)\\r\\n    BoundingBox - The bounding box. If specified, only pixels \\r\\n      located inside the bounding box are thresholded, pixels \\r\\n      outside are ignored. If not specified the whole image set is \\r\\n      thresholded. The bounding box is defined by the minimum and \\r\\n      maximum corners, MinCorner and MaxCorner.\\r\\n      Example:\\r\\n         To consider the bounding box defined by the points (x_min, \\r\\n      y_min, z_min) and (x_max, y_max, z_max), set \\r\\n      BoundingBox={\\\"MinCorner\\\":{'x':x_min, 'y':y_min, 'z':z_min}, \\r\\n      'MaxCorner':{'x':x_max, 'y':y_max, 'z':z_max}}\\r\\n\"}")
