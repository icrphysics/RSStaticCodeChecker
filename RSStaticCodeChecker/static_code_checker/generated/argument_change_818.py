import lib.lib as lib
import json
def easyCheck(s):
    return "CreateSphereGeometry" in s
def scoreForDict(d):
    import sys
    if not isinstance(d, dict):
        return sys.maxint
    arguments_right_result = argumentsRight(d)
    if arguments_right_result != True:
        return (float(arguments_right_result) + float(prefixScore(d)))/2.0
    return sys.maxint
def argumentsRight(d):
    args = ["Radius","Examination","Center","VoxelSize"]
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
    score_temp = lib.score_generic(d, "CreateSphereGeometry")
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    steps += 1
    score_temp = lib.score_generic(d.get("value"), "OfPoi")
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
    score_temp = lib.score_generic(d.get("value").get("value").get("value"), "ApprovedPoiStructures")
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    steps += 1
    score_temp = lib.score_generic(d.get("value").get("value").get("value").get("value"), "DependentApprovedStructureSet")
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    steps += 1
    score_temp = score_BeamSet.get_score(d.get("value").get("value").get("value").get("value").get("value"))
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    return float(score) / float(steps)
def get_info():
    return json.loads("{\"base\": \"BeamSet.DependentApprovedStructureSet.ApprovedPoiStructures.[].OfPoi\", \"params\": [\"Radius\", \"Examination\", \"Center\", \"VoxelSize\"], \"method\": \"CreateSphereGeometry\", \"description\": \"CreateSphereGeometry(..)\\r\\n  Create a sphere geometry for the current ROI.\\r\\n  Parameters:\\r\\n    Radius - The radius (cm) of the sphere geometry.\\r\\n    Examination - The examination where the geometry is created.\\r\\n    Center - The center coordinate (cm) of the geometry in the \\r\\n      DICOM patient-based coordinate system.\\r\\n    VoxelSize - The desired uniform voxel size (cm). Must be \\r\\n      between 0.01 and 1.0 cm. The default value is None which means \\r\\n      that a size dependent default voxel size is used. \\r\\n      Note that a explicitly setting a small voxel size for large \\r\\n      objects may lead to performance problems due to memory \\r\\n      limitations.\\r\\n\"}")
