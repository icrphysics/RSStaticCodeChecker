import lib.lib as lib
import json
def easyCheck(s):
    return "MapRoiGeometriesDeformably" in s
def scoreForDict(d):
    import sys
    if not isinstance(d, dict):
        return sys.maxint
    arguments_right_result = argumentsRight(d)
    if arguments_right_result != True:
        return (float(arguments_right_result) + float(prefixScore(d)))/2.0
    return sys.maxint
def argumentsRight(d):
    args = ["RoiGeometryNames","CreateNewRois","StructureRegistrationGroupNames","ReferenceExaminationNames","TargetExaminationNames","ReverseMapping","AbortWhenBadDisplacementField"]
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
    score_temp = lib.score_generic(d, "MapRoiGeometriesDeformably")
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
    return json.loads("{\"base\": \"Case\", \"params\": [\"RoiGeometryNames\", \"CreateNewRois\", \"StructureRegistrationGroupNames\", \"ReferenceExaminationNames\", \"TargetExaminationNames\", \"ReverseMapping\", \"AbortWhenBadDisplacementField\"], \"method\": \"MapRoiGeometriesDeformably\", \"description\": \"MapRoiGeometriesDeformably(..)\\r\\n  Map ROI geometries according to selected deformable \\r\\n  registration(s).\\r\\n  Parameters:\\r\\n    RoiGeometryNames - The names of the ROI geometries to map.\\r\\n    CreateNewRois - If true: for each RoiGeometry selected to \\r\\n      be mapped, a new ROI is created with geometries defined in \\r\\n      both the reference and the target image. The geometry in the \\r\\n      reference image is the same as the original and the geometry \\r\\n      in the target image is the mapped geometry. A suffix is added \\r\\n      to the ROI name.\\r\\n      If false: for each RoiGeometry selected a geometry is created \\r\\n      in the target image corresponding to the geometry mapped from \\r\\n      the reference image.\\r\\n      Default is false.\\r\\n    StructureRegistrationGroupNames - The name(s) of the \\r\\n      deformable registration group(s) to use for mapping.\\r\\n    ReferenceExaminationNames - The name(s) of the image(s) \\r\\n      where the deformation field(s) is defined.\\r\\n    TargetExaminationNames - The name(s) of the image(s) that \\r\\n      the deformation field(s) points to.\\r\\n    ReverseMapping - If true, geometries defined on the target \\r\\n      image are mapped to the reference image.\\r\\n      If false, geometries defined on the reference image are mapped \\r\\n      to the target image.\\r\\n      Default value is false.\\r\\n    AbortWhenBadDisplacementField - If true, geometries will \\r\\n      not be mapped if inverted deformation grid elements are \\r\\n      detected.\\r\\n      Default value is false.\\r\\n\"}")
