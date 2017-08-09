import lib.lib as lib
import json
def easyCheck(s):
    return "RoiSurfaceToSurfaceDistanceBasedOnDT" in s
def scoreForDict(d):
    import sys
    if not isinstance(d, dict):
        return sys.maxint
    arguments_right_result = argumentsRight(d)
    if arguments_right_result != True:
        return (float(arguments_right_result) + float(prefixScore(d)))/2.0
    return sys.maxint
def argumentsRight(d):
    args = ["ReferenceRoiName","TargetRoiName"]
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
    from bases import score_PatientDB
    steps += 1
    score_temp = lib.score_generic(d, "RoiSurfaceToSurfaceDistanceBasedOnDT")
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
    score_temp = lib.score_generic(d.get("value").get("value"), "StructureSets")
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    steps += 1
    score_temp = lib.score_generic(d.get("value").get("value").get("value"), "PatientModel")
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
    score_temp = lib.score_generic(d.get("value").get("value").get("value").get("value").get("value"), "TemplatePatientModels")
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    steps += 1
    score_temp = score_PatientDB.get_score(d.get("value").get("value").get("value").get("value").get("value").get("value"))
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    return float(score) / float(steps)
def get_info():
    return json.loads("{\"base\": \"PatientDB.TemplatePatientModels.[].PatientModel.StructureSets.[]\", \"params\": [\"ReferenceRoiName\", \"TargetRoiName\"], \"method\": \"RoiSurfaceToSurfaceDistanceBasedOnDT\", \"description\": \"RoiSurfaceToSurfaceDistanceBasedOnDT(..)\\r\\n  Measures the distance between the surfaces of two ROI geometries \\r\\n  using a distance transform based approach. \\r\\n  Each point (/voxel) on the surface of the target roi will be \\r\\n  assigned the minimum distance to a point (/voxel) on the surface \\r\\n  of the reference roi. \\r\\n  Note that the measurements are not symmetric\\r\\n  A dictionary with average, max and min distances are returned\\r\\n  Parameters:\\r\\n    ReferenceRoiName - Name of roi from which surface to \\r\\n      compute the distance\\r\\n    TargetRoiName - Name of roi to which surface to compute \\r\\n      the distance\\r\\n  Returns:\\r\\n    A dictionary with \\\"Average\\\", \\\"Max\\\", and \\\"Min\\\" distances\\r\\n\"}")
