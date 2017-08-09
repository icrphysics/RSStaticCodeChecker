import lib.lib as lib
import json
def easyCheck(s):
    return "OutlineBodyOnCBCT" in s
def scoreForDict(d):
    import sys
    if not isinstance(d, dict):
        return sys.maxint
    arguments_right_result = argumentsRight(d)
    if arguments_right_result != True:
        return (float(arguments_right_result) + float(prefixScore(d)))/2.0
    return sys.maxint
def argumentsRight(d):
    args = ["ModelExaminationName","ThresholdLevel","FieldOfViewRoiName","ExternalMbsRoiName","SupInfRange"]
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
    score_temp = lib.score_generic(d, "OutlineBodyOnCBCT")
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
    score_temp = lib.score_generic(d.get("value").get("value"), "StructureSets")
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    steps += 1
    score_temp = lib.score_generic(d.get("value").get("value").get("value"), "PatientModel")
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    steps += 1
    score_temp = score_Case.get_score(d.get("value").get("value").get("value").get("value"))
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    return float(score) / float(steps)
def get_info():
    return json.loads("{\"base\": \"Case.PatientModel.StructureSets.[]\", \"params\": [\"ModelExaminationName\", \"ThresholdLevel\", \"FieldOfViewRoiName\", \"ExternalMbsRoiName\", \"SupInfRange\"], \"method\": \"OutlineBodyOnCBCT\", \"description\": \"OutlineBodyOnCBCT(..)\\r\\n  Creates geometry for the External ROI for a limited \\r\\n  field-of-view CBCT examination.\\r\\n  Parameters:\\r\\n    ModelExaminationName - The name of the examination that \\r\\n      will be used as the model. Typically, the planning CT.\\r\\n      The External ROI must have geometry defined for this \\r\\n      examination.\\r\\n    ThresholdLevel - The threshold level used to guide an MBS \\r\\n      mesh based on the geometry of the External ROI for the \\r\\n      model examination. This value should be chosen such that \\r\\n      larger values correspond to \\r\\n      anatomy in the CBCT examination.\\r\\n    FieldOfViewRoiName - The name of the field-of-view ROI \\r\\n      geometry. This ROI defines the region in which\\r\\n      MBS adaptation is performed for the MBS mesh based on the \\r\\n      external geometry in the model\\r\\n      examination.\\r\\n    ExternalMbsRoiName - The name of the external MBS ROI.\\r\\n    SupInfRange - The sup/inf range used when creating the \\r\\n      model (in cm).\\r\\n      Should be given in CBCT coordinates.\\r\\n      If (0,0) is given, the whole external on the model examination \\r\\n      will be used.\\r\\n\"}")
