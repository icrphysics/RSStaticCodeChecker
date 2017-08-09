import lib.lib as lib
import json
def easyCheck(s):
    return "CreateControllingRoiGeometries" in s
def scoreForDict(d):
    import sys
    if not isinstance(d, dict):
        return sys.maxint
    arguments_right_result = argumentsRight(d)
    if arguments_right_result != True:
        return (float(arguments_right_result) + float(prefixScore(d)))/2.0
    return sys.maxint
def argumentsRight(d):
    args = ["ReferenceExaminationName","TargetExaminationNames","RoiGeometryNames","SmoothingRadius","DesiredTriangleEdgeLength","CreateNewRois"]
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
    from bases import score_Patient
    steps += 1
    score_temp = lib.score_generic(d, "CreateControllingRoiGeometries")
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    steps += 1
    score_temp = lib.score_generic(d.get("value"), "PatientModel")
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
    score_temp = lib.score_generic(d.get("value").get("value").get("value"), "Cases")
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    steps += 1
    score_temp = score_Patient.get_score(d.get("value").get("value").get("value").get("value"))
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    return float(score) / float(steps)
def get_info():
    return json.loads("{\"base\": \"Patient.Cases.[].PatientModel\", \"params\": [\"ReferenceExaminationName\", \"TargetExaminationNames\", \"RoiGeometryNames\", \"SmoothingRadius\", \"DesiredTriangleEdgeLength\", \"CreateNewRois\"], \"method\": \"CreateControllingRoiGeometries\", \"description\": \"CreateControllingRoiGeometries(..)\\r\\n  Creates controlling ROI geometries for reference and target \\r\\n  examinations.\\r\\n  Parameters:\\r\\n    ReferenceExaminationName - The name of the examination for \\r\\n      which to create the controlling roi meshes.\\r\\n    TargetExaminationNames - The names of the examinations on \\r\\n      which to create controlling roi geometries based on the meshes \\r\\n      created on the reference examination.\\r\\n    RoiGeometryNames - The name of the roi geometry which the \\r\\n      controlling roi should adapt to.\\r\\n    SmoothingRadius - Applies a morphological close and open \\r\\n      with a structuring element of the given radius \\r\\n      (in cm) before creating / adapting the triangle mesh. If set \\r\\n      to 0, no smoothing will be done\\r\\n    DesiredTriangleEdgeLength - Desired edge length (in cm) \\r\\n      for the triangles in the mesh created on the reference \\r\\n      examination.\\r\\n      Voxel size 0.1 x 0.1 x 0.1 will be used and a typical value \\r\\n      for DesiredTriangleEdgeLength is 0.3\\r\\n    CreateNewRois - If true, the controlling roi meshes will \\r\\n      be placed in a new roi.\\r\\n      If false, the controlling roi meshes will overwrite existing \\r\\n      roi geometries.\\r\\n\"}")
