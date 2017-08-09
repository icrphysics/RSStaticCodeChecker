import lib.lib as lib
import json
def easyCheck(s):
    return "ImportSegmentationAsMetaImage" in s
def scoreForDict(d):
    import sys
    if not isinstance(d, dict):
        return sys.maxint
    arguments_right_result = argumentsRight(d)
    if arguments_right_result != True:
        return (float(arguments_right_result) + float(prefixScore(d)))/2.0
    return sys.maxint
def argumentsRight(d):
    args = ["MetaFileName","RoiNamesAndLabels","UseGreaterOrEqual"]
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
    score_temp = lib.score_generic(d, "ImportSegmentationAsMetaImage")
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
    return json.loads("{\"base\": \"Case.PatientModel.StructureSets.[]\", \"params\": [\"MetaFileName\", \"RoiNamesAndLabels\", \"UseGreaterOrEqual\"], \"method\": \"ImportSegmentationAsMetaImage\", \"description\": \"ImportSegmentationAsMetaImage(..)\\r\\n  Import segmentation as meta image file \\r\\n  (http://www.itk.org/Wiki/ITK/MetaIO/Documentation).\\r\\n              \\r\\n  Note that meta image file uses mm as unit. Hence \\r\\n  Offset/Position/Origin and ElementSize/ElementSpacing should be \\r\\n  given in mm.\\r\\n  This method is for experimental use - use with care.\\r\\n  Parameters:\\r\\n    MetaFileName - File name\\r\\n    RoiNamesAndLabels - Dictionary containing wanted ROI names \\r\\n      and their corresponding labels in the meta image\\r\\n    UseGreaterOrEqual - Default false. If true, ROI will be \\r\\n      equal to all voxels with values >= label\\r\\n\"}")
