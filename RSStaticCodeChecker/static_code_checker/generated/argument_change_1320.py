import lib.lib as lib
import json
def easyCheck(s):
    return "UpdateDerivedGeometries" in s
def scoreForDict(d):
    import sys
    if not isinstance(d, dict):
        return sys.maxint
    arguments_right_result = argumentsRight(d)
    if arguments_right_result != True:
        return (float(arguments_right_result) + float(prefixScore(d)))/2.0
    return sys.maxint
def argumentsRight(d):
    args = ["RoiNames","Examination","Algorithm","AreEmptyDependenciesAllowed"]
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
    score_temp = lib.score_generic(d, "UpdateDerivedGeometries")
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
    score_temp = score_Case.get_score(d.get("value").get("value"))
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    return float(score) / float(steps)
def get_info():
    return json.loads("{\"base\": \"Case.PatientModel\", \"params\": [\"RoiNames\", \"Examination\", \"Algorithm\", \"AreEmptyDependenciesAllowed\"], \"method\": \"UpdateDerivedGeometries\", \"description\": \"UpdateDerivedGeometries(..)\\r\\n  Updates the derived geometry for the specified examination.\\r\\n  Parameters:\\r\\n    RoiNames - The ROIs to update.\\r\\n    Examination - The target examination.\\r\\n    Algorithm - Defines if the logical set operations use \\r\\n      contour or voxel based methods. \\r\\n      Margins (expand/contract) and Wall operations are always \\r\\n      performed using voxel based methods.\\r\\n                  \\r\\n      Possible values:\\r\\n      * Auto: Automatically select algorithm mode.\\r\\n      * Contours: Use contour based methods.\\r\\n      * Voxels: Use voxel based methods.\\r\\n      Default value is \\\"Auto\\\".\\r\\n    AreEmptyDependenciesAllowed - If empty dependencies are \\r\\n      not allowed the resulting derived status will be set to 'Needs \\r\\n      update'\\r\\n      if any of the geometries that an ROI depends on are empty.\\r\\n\"}")
