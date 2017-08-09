import lib.lib as lib
import json
def easyCheck(s):
    return "MapRoiGeometriesRigidly" in s
def scoreForDict(d):
    import sys
    if not isinstance(d, dict):
        return sys.maxint
    arguments_right_result = argumentsRight(d)
    if arguments_right_result != True:
        return (float(arguments_right_result) + float(prefixScore(d)))/2.0
    return sys.maxint
def argumentsRight(d):
    args = ["RoiGeometryNames","CreateNewRois","ReferenceExaminationName","TargetExaminationNames","Transformations"]
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
    score_temp = lib.score_generic(d, "MapRoiGeometriesRigidly")
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
    score_temp = lib.score_generic(d.get("value").get("value"), "Cases")
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    steps += 1
    score_temp = score_Patient.get_score(d.get("value").get("value").get("value"))
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    return float(score) / float(steps)
def get_info():
    return json.loads("{\"base\": \"Patient.Cases.[]\", \"params\": [\"RoiGeometryNames\", \"CreateNewRois\", \"ReferenceExaminationName\", \"TargetExaminationNames\", \"Transformations\"], \"method\": \"MapRoiGeometriesRigidly\", \"description\": \"MapRoiGeometriesRigidly(..)\\r\\n  Map ROI geometries according to selected transformation(s).\\r\\n  Parameters:\\r\\n    RoiGeometryNames - The names of the ROI geometries to map.\\r\\n    CreateNewRois - If true: for each RoiGeometry selected to \\r\\n      be mapped, a new ROI is created with geometries defined in \\r\\n      both the reference and the target image. The geometry in the \\r\\n      reference image is the same as the original and the geometry \\r\\n      in the target image is the mapped geometry. A suffix is added \\r\\n      to the ROI name.\\r\\n      If false: for each RoiGeometry selected a geometry is created \\r\\n      in the target image corresponding to the geometry mapped from \\r\\n      the reference image.\\r\\n      Default is false.\\r\\n    ReferenceExaminationName - The name of the image from \\r\\n      which the transformation(s) is defined.\\r\\n    TargetExaminationNames - The name(s) of the image(s) that \\r\\n      the deformation field(s) points to.\\r\\n    Transformations - The transformation(s) from the reference \\r\\n      image(s) to the target image(s).\\r\\n      Transformations are given in homogeneous coordinates, e.g., \\r\\n      the identity transform is \\r\\n      {'M11' : 1, 'M12': 0, 'M13': 0, 'M14': 0, \\\\\\r\\n      'M21' : 0, 'M22': 1, 'M23': 0, 'M24': 0, \\\\\\r\\n      'M31' : 0, 'M32': 0, 'M33': 1, 'M34': 0,\\\\\\r\\n      'M41' : 0, 'M42': 0, 'M43': 0, 'M44': 1}\\r\\n\"}")
