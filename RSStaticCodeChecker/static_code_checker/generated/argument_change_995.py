import lib.lib as lib
import json
def easyCheck(s):
    return "ComparisonOfRoiGeometries" in s
def scoreForDict(d):
    import sys
    if not isinstance(d, dict):
        return sys.maxint
    arguments_right_result = argumentsRight(d)
    if arguments_right_result != True:
        return (float(arguments_right_result) + float(prefixScore(d)))/2.0
    return sys.maxint
def argumentsRight(d):
    args = ["RoiA","RoiB","ComputeDistanceToAgreementMeasures"]
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
    score_temp = lib.score_generic(d, "ComparisonOfRoiGeometries")
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    steps += 1
    score_temp = lib.score_generic(d.get("value"), "OutlineSource")
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
    return json.loads("{\"base\": \"BeamSet.DrrSettings.[].BeamListSource.FractionDose.BeamDoses.[].OnDensity.OutlineSource\", \"params\": [\"RoiA\", \"RoiB\", \"ComputeDistanceToAgreementMeasures\"], \"method\": \"ComparisonOfRoiGeometries\", \"description\": \"ComparisonOfRoiGeometries(..)\\r\\n   Computes overlap measures between two geometries for comparison.\\r\\n   \\r\\n   Dice similarity coefficient/index - DSC (also called Dice's \\r\\n  coefficient or Sorensen index): \\r\\n             2 | ROIA intersect ROIB | / | ROIA | + | ROIB |\\r\\n   DSC range between 0 (no overlap) and 1 (complete overlap)\\r\\n   DSC with reference to:\\r\\n   Dice, \\\"Measures of the amount of ecologic association between \\r\\n  species\\\", Ecology 26:297\\u2013302 (1945)\\r\\n              \\r\\n   Precision:\\r\\n            | ROIA intersect ROIB | / | ROIA union ROIB |\\r\\n   Precision range between 0 (no overlap) and 1 (complete overlap)\\r\\n   Precision with reference to:\\r\\n   Udupa et al, \\\"A framework for evaluating image segmentation \\r\\n  algorithms\\\", Computerized Medical Imaging and Graphics, \\r\\n  30(2):75-87 (2006)\\r\\n              \\r\\n   Specificity:\\r\\n            1 - | ROIB not ROIA | / | ROIA |\\r\\n   Specificity is 1 for a complete overlap, and otherwise less than 1\\r\\n   Delineation specificity with reference to:\\r\\n   Udupa et al, \\\"A framework for evaluating image segmentation \\r\\n  algorithms\\\", Computerized Medical Imaging and Graphics, \\r\\n  30(2):75-87 (2006)\\r\\n              \\r\\n   Sensitivity:\\r\\n            | ROIA intersect ROIB | / | ROIA |\\r\\n   Sensitivity range between 0 (no overlap) and 1 (complete overlap)\\r\\n   Delineation sensitivity with reference to:\\r\\n   Udupa et al, \\\"A framework for evaluating image segmentation \\r\\n  algorithms\\\", Computerized Medical Imaging and Graphics, \\r\\n  30(2):75-87 (2006)\\r\\n              \\r\\n   Mean distance to agreement (Mean DTA):\\r\\n   Average distance for the surface of ROIA intersect ROIB to the \\r\\n  surface of ROIA union ROIB\\r\\n   Measured using a distance transform based approach. Each point \\r\\n  (/voxel) on the surface of the target roi will be assigned the \\r\\n  minimum distance to a point (/voxel) on the surface of the \\r\\n  reference roi. \\r\\n   Mean DTA is 0 for complete overlap. If no overlap, infinity is \\r\\n  assigned.\\r\\n   Unit is cm.\\r\\n   Note: If the Mean DTA has not been computed there will be no \\r\\n  corresponding entry in the return value.\\r\\n              \\r\\n   Max distance to agreement (Max DTA):\\r\\n   Maximum distance for the surface of ROIA intersect ROIB to the \\r\\n  surface of ROIA union ROIB\\r\\n   Measured using a distance transform based approach. Each point \\r\\n  (/voxel) on the surface of the target roi will be assigned the \\r\\n  minimum distance to a point (/voxel) on the surface of the \\r\\n  reference roi. \\r\\n   Max DTA is 0 for complete overlap. If no overlap, infinity is \\r\\n  assigned.\\r\\n   Unit is cm.\\r\\n   Note: If the Max DTA has not been computed there will be no \\r\\n  corresponding entry in the return value.\\r\\n  Parameters:\\r\\n    RoiA - The name of the ROI geometry A.\\r\\n    RoiB - The name of the ROI geometry B.\\r\\n    ComputeDistanceToAgreementMeasures - Determines if Mean \\r\\n      DTA and Max DTA are computed (computation time will increase).\\r\\n      If set to false, Mean DTA and Max DTA will not have \\r\\n      corresponding key/value entries in the return value.\\r\\n\"}")
