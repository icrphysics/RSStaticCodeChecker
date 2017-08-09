import lib.lib as lib
import json
def easyCheck(s):
    return "ComputeRigidImageRegistration" in s
def scoreForDict(d):
    import sys
    if not isinstance(d, dict):
        return sys.maxint
    arguments_right_result = argumentsRight(d)
    if arguments_right_result != True:
        return (float(arguments_right_result) + float(prefixScore(d)))/2.0
    return sys.maxint
def argumentsRight(d):
    args = ["FloatingExaminationName","ReferenceExaminationName","UseOnlyTranslations","HighWeightOnBones","InitializeImages","FocusRoisNames","RegistrationName"]
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
    score_temp = lib.score_generic(d, "ComputeRigidImageRegistration")
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
    return json.loads("{\"base\": \"Case\", \"params\": [\"FloatingExaminationName\", \"ReferenceExaminationName\", \"UseOnlyTranslations\", \"HighWeightOnBones\", \"InitializeImages\", \"FocusRoisNames\", \"RegistrationName\"], \"method\": \"ComputeRigidImageRegistration\", \"description\": \"ComputeRigidImageRegistration(..)\\r\\n  Computes a rigid image registration.\\r\\n  Parameters:\\r\\n    FloatingExaminationName - The name of the floating \\r\\n      examination which is rigidly transformed.\\r\\n    ReferenceExaminationName - The name of the reference \\r\\n      examination which is not transformed.\\r\\n    UseOnlyTranslations - Set to \\\"true\\\" if rotations shall be \\r\\n      discarded in the registration process.\\r\\n    HighWeightOnBones - Set to \\\"true\\\" if the registration \\r\\n      algorithm shall focus on bony structures.\\r\\n    InitializeImages - Set to \\\"true\\\" if the registration \\r\\n      algorithm shall try to find an approximate registration before \\r\\n      the accurate registration is computed.\\r\\n    FocusRoisNames - Names of the focus ROIs.\\r\\n    RegistrationName - Name of the registration. Only \\r\\n      applicable if an additional rigid registration is computed. In \\r\\n      case a frame-of-reference registration is created the name \\r\\n      will not be used and can be left empty.\\r\\n\"}")
