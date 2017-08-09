import lib.lib as lib
import json
def easyCheck(s):
    return "MapPoiGeometriesDeformably" in s
def scoreForDict(d):
    import sys
    if not isinstance(d, dict):
        return sys.maxint
    arguments_right_result = argumentsRight(d)
    if arguments_right_result != True:
        return (float(arguments_right_result) + float(prefixScore(d)))/2.0
    return sys.maxint
def argumentsRight(d):
    args = ["PoiGeometryNames","CreateNewPois","StructureRegistrationGroupNames","ReferenceExaminationNames","TargetExaminationNames","ReverseMapping","AbortWhenBadDisplacementField"]
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
    score_temp = lib.score_generic(d, "MapPoiGeometriesDeformably")
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
    return json.loads("{\"base\": \"Case\", \"params\": [\"PoiGeometryNames\", \"CreateNewPois\", \"StructureRegistrationGroupNames\", \"ReferenceExaminationNames\", \"TargetExaminationNames\", \"ReverseMapping\", \"AbortWhenBadDisplacementField\"], \"method\": \"MapPoiGeometriesDeformably\", \"description\": \"MapPoiGeometriesDeformably(..)\\r\\n  Map POI geometries according to selected deformable \\r\\n  registration(s).\\r\\n  Parameters:\\r\\n    PoiGeometryNames - The names of the POI geometries to map.\\r\\n    CreateNewPois - If true: for each PoiGeometry selected to \\r\\n      be mapped, a new POI is created with geometries (points) \\r\\n      defined in both the reference and the target image. The \\r\\n      geometry in the reference image is the same as the original \\r\\n      and the geometry in the target image is the mapped geometry. A \\r\\n      suffix is added to the POI name.\\r\\n      If false: for each PoiGeometry selected, a geometry (point) is \\r\\n      created in the target image corresponding to the mapped \\r\\n      position.\\r\\n      Default is false.\\r\\n    StructureRegistrationGroupNames - The name(s) of the \\r\\n      deformable registration group(s) to use for mapping.\\r\\n    ReferenceExaminationNames - The name(s) of the image(s) \\r\\n      where the deformation field(s) is defined.\\r\\n    TargetExaminationNames - The name(s) of the image(s) that \\r\\n      the deformation field(s) points to.\\r\\n    ReverseMapping - If true, geometries defined on the target \\r\\n      image are mapped to the reference image.\\r\\n      If false, geometries defined on the reference image are mapped \\r\\n      to the target image.\\r\\n      Default value is false.\\r\\n    AbortWhenBadDisplacementField - If true, geometries will \\r\\n      not be mapped if inverted deformation grid elements are \\r\\n      detected.\\r\\n      Default value is false.\\r\\n\"}")
