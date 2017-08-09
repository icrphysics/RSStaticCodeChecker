import lib.lib as lib
import json
def easyCheck(s):
    return "RunReduceOARDoseOptimization" in s
def scoreForDict(d):
    import sys
    if not isinstance(d, dict):
        return sys.maxint
    arguments_right_result = argumentsRight(d)
    if arguments_right_result != True:
        return (float(arguments_right_result) + float(prefixScore(d)))/2.0
    return sys.maxint
def argumentsRight(d):
    args = ["UseVoxelBasedMimickingForTargets","UseVoxelBasedMimickingForOrgansAtRisk","OrgansAtRiskToImprove","TargetsToMaintain","OrgansAtRiskToMaintain"]
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
    score_temp = lib.score_generic(d, "RunReduceOARDoseOptimization")
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
    score_temp = lib.score_generic(d.get("value").get("value"), "PlanOptimizations")
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
    score_temp = lib.score_generic(d.get("value").get("value").get("value").get("value"), "TreatmentPlans")
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    steps += 1
    score_temp = lib.score_generic(d.get("value").get("value").get("value").get("value").get("value"), "[]")
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    steps += 1
    score_temp = lib.score_generic(d.get("value").get("value").get("value").get("value").get("value").get("value"), "Cases")
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    steps += 1
    score_temp = score_Patient.get_score(d.get("value").get("value").get("value").get("value").get("value").get("value").get("value"))
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    return float(score) / float(steps)
def get_info():
    return json.loads("{\"base\": \"Patient.Cases.[].TreatmentPlans.[].PlanOptimizations.[]\", \"params\": [\"UseVoxelBasedMimickingForTargets\", \"UseVoxelBasedMimickingForOrgansAtRisk\", \"OrgansAtRiskToImprove\", \"TargetsToMaintain\", \"OrgansAtRiskToMaintain\"], \"method\": \"RunReduceOARDoseOptimization\", \"description\": \"RunReduceOARDoseOptimization(..)\\r\\n  Runs a reduce organ-at-risk optimization.\\r\\n  Auto-generated reference dose functions are used to reduce the \\r\\n  dose in \\r\\n  the organs-at-risk regions while maintaining dose homogeneity in \\r\\n  the target regions.\\r\\n  Parameters:\\r\\n    UseVoxelBasedMimickingForTargets - Indicates if voxel \\r\\n      based mimicking constraints should be used for target ROIs.\\r\\n      If false, DVH based mimicking constraints is used for target \\r\\n      ROIs.\\r\\n      Default is false.\\r\\n    UseVoxelBasedMimickingForOrgansAtRisk - Indicates if \\r\\n      voxel-based mimicking constraints should be used for \\r\\n      organ-at-risk ROIs.\\r\\n      If false, DVH-based mimicking constraints is used for \\r\\n      organ-at-risk ROIs.\\r\\n      Default is false.\\r\\n    OrgansAtRiskToImprove - Names of the ROIs that should be \\r\\n      considered as objectives in the optimization problem.\\r\\n      Must be a subset of OrgansAtRiskToMaintain.\\r\\n      Default is ROIs defined in OrgansAtRiskToMaintain.\\r\\n    TargetsToMaintain - Names of the ROIs that should be \\r\\n      considered as target ROIs in the optimization problem.\\r\\n      The optimization uses mimicking constraints to maintain the \\r\\n      uniformity of the dose for these ROIs.\\r\\n      Must be disjoint with OrgansAtRiskToMaintain.\\r\\n      Default is all ROIs with target optimization functions in the \\r\\n      original optimization problem.\\r\\n    OrgansAtRiskToMaintain - Names of the ROIs that should be \\r\\n      considered as organs-at-risk in the optimization problem.\\r\\n      The optimization uses mimicking constraints to avoid \\r\\n      increasing the dose for these ROIs.\\r\\n      Must be disjoint with TargetsToMaintain.\\r\\n      Default is all ROIs without target optimization functions in \\r\\n      the original optimization problem.\\r\\n\"}")
