import lib.lib as lib
import json
def easyCheck(s):
    return "MultiSpectralThreshold" in s
def scoreForDict(d):
    import sys
    if not isinstance(d, dict):
        return sys.maxint
    arguments_right_result = argumentsRight(d)
    if arguments_right_result != True:
        return (float(arguments_right_result) + float(prefixScore(d)))/2.0
    return sys.maxint
def argumentsRight(d):
    args = ["ExaminationNames","LowThresholds","HighThresholds"]
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
    score_temp = lib.score_generic(d, "MultiSpectralThreshold")
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
    score_temp = lib.score_generic(d.get("value").get("value"), "OutlineRoiGeometry")
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
    score_temp = lib.score_generic(d.get("value").get("value").get("value").get("value"), "StructureSets")
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    steps += 1
    score_temp = lib.score_generic(d.get("value").get("value").get("value").get("value").get("value"), "PatientModel")
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    steps += 1
    score_temp = score_Case.get_score(d.get("value").get("value").get("value").get("value").get("value").get("value"))
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    return float(score) / float(steps)
def get_info():
    return json.loads("{\"base\": \"Case.PatientModel.StructureSets.[].OutlineRoiGeometry.OfRoi\", \"params\": [\"ExaminationNames\", \"LowThresholds\", \"HighThresholds\"], \"method\": \"MultiSpectralThreshold\", \"description\": \"MultiSpectralThreshold(..)\\r\\n  Multispectral thresholding of examinations in a MR protocol \\r\\n  group. \\r\\n  For each examination, LowThreshold and HighThreshold should be \\r\\n  given. \\r\\n  The resulting segmented region will consist of points which are in \\r\\n  the given (examination specific) range for each examination.\\r\\n  RoiGeometries will be created on each examination.\\r\\n  Parameters:\\r\\n    ExaminationNames - The examination names. All selected \\r\\n      examinations need to be in the same MR protocol group\\r\\n    LowThresholds - The low thresholds - one for each of the \\r\\n      selected examinations\\r\\n    HighThresholds - The high thresholds - one for each of the \\r\\n      selected examinations\\r\\n\"}")
