import lib.lib as lib
import json
def easyCheck(s):
    return "OutlineMbsMesh" in s
def scoreForDict(d):
    import sys
    if not isinstance(d, dict):
        return sys.maxint
    arguments_right_result = argumentsRight(d)
    if arguments_right_result != True:
        return (float(arguments_right_result) + float(prefixScore(d)))/2.0
    return sys.maxint
def argumentsRight(d):
    args = ["ExternalMbsRoiName","ExternalMbsRoiColor","ModelExaminationName","TargetExaminationNames","SuperiorInferiorRange","UseExistingExternalMbsModel"]
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
    score_temp = lib.score_generic(d, "OutlineMbsMesh")
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
    return json.loads("{\"base\": \"Patient.Cases.[]\", \"params\": [\"ExternalMbsRoiName\", \"ExternalMbsRoiColor\", \"ModelExaminationName\", \"TargetExaminationNames\", \"SuperiorInferiorRange\", \"UseExistingExternalMbsModel\"], \"method\": \"OutlineMbsMesh\", \"description\": \"OutlineMbsMesh(..)\\r\\n  Creates an external MBS model based on the external geometry on \\r\\n  the \\\"model examination\\\" and stores it in the data base (for future \\r\\n  use).\\r\\n  Create external MBS meshes for the selected images based on the \\r\\n  external MBS model.\\r\\n  Parameters:\\r\\n    ExternalMbsRoiName - The name of the external MBS ROI to \\r\\n      create.\\r\\n    ExternalMbsRoiColor - The color of the external MBS ROI to \\r\\n      create.\\r\\n      Default value is Yellow.\\r\\n    ModelExaminationName - The name of the examination used to \\r\\n      create an outline MBS model from.\\r\\n    TargetExaminationNames - The name(s) of the examination(s) \\r\\n      for which to create an outline MBS roigeometry.\\r\\n    SuperiorInferiorRange - The sup-inf range interval for \\r\\n      which the external MBS should be defined for (on the model \\r\\n      examination geometry).\\r\\n      If SuperiorInferiorRange is set to [0,0] the range covered by \\r\\n      the complete external geometry will be used.\\r\\n      Use the script extension utility method \\r\\n      StructureSet.GetSuperiorInferiorRangeForExternalGeometry() for \\r\\n      guidance when a smaller range is wanted.\\r\\n    UseExistingExternalMbsModel - If to use an existing \\r\\n      external MBS model.\\r\\n      If an external MBS model exists and \\r\\n      UseExistingExternalMbsModel == false, the model stored in the \\r\\n      data base is removed and a new is created.\\r\\n      This option can only be used if no external MBS geometries \\r\\n      exist (i.e., when the external MBS ROI has been removed).\\r\\n\"}")
