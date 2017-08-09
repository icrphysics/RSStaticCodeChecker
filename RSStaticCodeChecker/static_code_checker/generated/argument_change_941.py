import lib.lib as lib
import json
def easyCheck(s):
    return "ExportRoiGeometryAsMetaImageWithSpecifiedGridSettings" in s
def scoreForDict(d):
    import sys
    if not isinstance(d, dict):
        return sys.maxint
    arguments_right_result = argumentsRight(d)
    if arguments_right_result != True:
        return (float(arguments_right_result) + float(prefixScore(d)))/2.0
    return sys.maxint
def argumentsRight(d):
    args = ["MetaFileName","VoxelSize","Corner","NumberOfVoxels"]
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
    score_temp = lib.score_generic(d, "ExportRoiGeometryAsMetaImageWithSpecifiedGridSettings")
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    steps += 1
    score_temp = lib.score_generic(d.get("value"), "OutlineGeometry")
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    steps += 1
    score_temp = lib.score_generic(d.get("value").get("value"), "OnDensity")
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
    score_temp = lib.score_generic(d.get("value").get("value").get("value").get("value"), "BeamDoses")
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    steps += 1
    score_temp = lib.score_generic(d.get("value").get("value").get("value").get("value").get("value"), "FractionDose")
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    steps += 1
    score_temp = lib.score_generic(d.get("value").get("value").get("value").get("value").get("value").get("value"), "BeamListSource")
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    steps += 1
    score_temp = lib.score_generic(d.get("value").get("value").get("value").get("value").get("value").get("value").get("value"), "[]")
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    steps += 1
    score_temp = lib.score_generic(d.get("value").get("value").get("value").get("value").get("value").get("value").get("value").get("value"), "DrrSettings")
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    steps += 1
    score_temp = score_BeamSet.get_score(d.get("value").get("value").get("value").get("value").get("value").get("value").get("value").get("value").get("value"))
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    return float(score) / float(steps)
def get_info():
    return json.loads("{\"base\": \"BeamSet.DrrSettings.[].BeamListSource.FractionDose.BeamDoses.[].OnDensity.OutlineGeometry\", \"params\": [\"MetaFileName\", \"VoxelSize\", \"Corner\", \"NumberOfVoxels\"], \"method\": \"ExportRoiGeometryAsMetaImageWithSpecifiedGridSettings\", \"description\": \"ExportRoiGeometryAsMetaImageWithSpecifiedGridSettings(..)\\r\\n   Export a roi geometry (using its voxel representation) as meta \\r\\n  image file (http://www.itk.org/Wiki/ITK/MetaIO/Documentation).\\r\\n   Dimensions are given by parameters VoxelSize, Corner and \\r\\n  NumberOfVoxels. \\r\\n   Note that the grid settings need to be such that the bounding box \\r\\n  of the geometry is covered.\\r\\n              \\r\\n   As the voxel representation is used voxels in the exported image \\r\\n  will have values between 0 and 255, \\r\\n   where 0 correspond to voxels outside the roi geometry, 255 to \\r\\n  voxels completely inside the roi geometry, and 1 - 254 to voxels \\r\\n  on the boundary of the roi geometry, describing the relative \\r\\n  belongingness to the roi geometry.\\r\\n   \\r\\n   Note that meta image file uses mm as unit. Hence \\r\\n  Offset/Position/Origin and ElementSize/ElementSpacing is given in \\r\\n  mm.\\r\\n  Parameters:\\r\\n    MetaFileName - File name\\r\\n    VoxelSize - Voxel size in the exported image\\r\\n    Corner - Corner for the exported image\\r\\n    NumberOfVoxels - Number of voxels in the exported image\\r\\n\"}")
