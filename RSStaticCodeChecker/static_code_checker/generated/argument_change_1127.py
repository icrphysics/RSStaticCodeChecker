import lib.lib as lib
import json
def easyCheck(s):
    return "CreateTransformedExamination" in s
def scoreForDict(d):
    import sys
    if not isinstance(d, dict):
        return sys.maxint
    arguments_right_result = argumentsRight(d)
    if arguments_right_result != True:
        return (float(arguments_right_result) + float(prefixScore(d)))/2.0
    return sys.maxint
def argumentsRight(d):
    args = ["ExaminationName","YawRotation","PitchRotation","RollRotation","Translation","FrameOfReference"]
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
    score_temp = lib.score_generic(d, "CreateTransformedExamination")
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
    return json.loads("{\"base\": \"PatientDB.TemplatePatientModels.[].PatientModel.StructureSets.[].OnExamination\", \"params\": [\"ExaminationName\", \"YawRotation\", \"PitchRotation\", \"RollRotation\", \"Translation\", \"FrameOfReference\"], \"method\": \"CreateTransformedExamination\", \"description\": \"CreateTransformedExamination(..)\\r\\n  Method for creating a rigidly transformed examination from an \\r\\n  existing.\\r\\n              \\r\\n  This method is for experimental use - use with care.\\r\\n  Parameters:\\r\\n    ExaminationName - Name given to the transformed examination\\r\\n    YawRotation - Rotation angle in yaw direction (around \\r\\n      ant-post)\\r\\n    PitchRotation - Rotation angle in pitch direction (around \\r\\n      left-right)\\r\\n    RollRotation - Rotation angle in roll direction (around \\r\\n      sup-inf)\\r\\n    Translation - Translation (in patient coordinate system: \\r\\n      r-l, i-s, p-a)\\r\\n    FrameOfReference - Frame-of-reference for the transformed \\r\\n      examination. If empty string is given the Frame-Of-Reference \\r\\n      will be set to the same as for the original examination\\r\\n  Returns:\\r\\n    \\r\\n\"}")
