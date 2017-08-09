import lib.lib as lib
import json
def easyCheck(s):
    return "GetStoredDicomTagValueForVerification" in s
def scoreForDict(d):
    import sys
    if not isinstance(d, dict):
        return sys.maxint
    arguments_right_result = argumentsRight(d)
    if arguments_right_result != True:
        return (float(arguments_right_result) + float(prefixScore(d)))/2.0
    return sys.maxint
def argumentsRight(d):
    args = ["Group","Element"]
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
    from bases import score_PatientDB
    steps += 1
    score_temp = lib.score_generic(d, "GetStoredDicomTagValueForVerification")
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    steps += 1
    score_temp = lib.score_generic(d.get("value"), "OnExamination")
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    steps += 1
    score_temp = lib.score_generic(d.get("value").get("value"), "[]")
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    steps += 1
    score_temp = lib.score_generic(d.get("value").get("value").get("value"), "StructureSets")
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    steps += 1
    score_temp = lib.score_generic(d.get("value").get("value").get("value").get("value"), "PatientModel")
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
    score_temp = lib.score_generic(d.get("value").get("value").get("value").get("value").get("value").get("value"), "TemplatePatientModels")
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    steps += 1
    score_temp = score_PatientDB.get_score(d.get("value").get("value").get("value").get("value").get("value").get("value").get("value"))
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    return float(score) / float(steps)
def get_info():
    return json.loads("{\"base\": \"PatientDB.TemplatePatientModels.[].PatientModel.StructureSets.[].OnExamination\", \"params\": [\"Group\", \"Element\"], \"method\": \"GetStoredDicomTagValueForVerification\", \"description\": \"GetStoredDicomTagValueForVerification(..)\\r\\n  Get the stored dicom tag value for verification. Tag is given as \\r\\n  group and element in hexadecimal format, \\r\\n  i.e., Group=0x0008, Element=0x0008 will give back attribute \\\"Image \\r\\n  Type\\\"\\r\\n              \\r\\n  Dicom sequence tags are currently not supported.\\r\\n              \\r\\n  One image slice is used to collect the requested information.\\r\\n  Hence, for tags with different values in different slices (SOP \\r\\n  Instance UID, Content time, Image Position etc), only one value \\r\\n  will be reported.\\r\\n  Parameters:\\r\\n    Group - Group (hexadecimal)\\r\\n    Element - Element (hexadecimal)\\r\\n  Returns:\\r\\n    Dictionary with description and value (as a string)\\r\\n\"}")
