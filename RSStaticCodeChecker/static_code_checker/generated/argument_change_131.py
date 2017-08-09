import lib.lib as lib
import json
def easyCheck(s):
    return "SetRigidTransformation" in s
def scoreForDict(d):
    import sys
    if not isinstance(d, dict):
        return sys.maxint
    arguments_right_result = argumentsRight(d)
    if arguments_right_result != True:
        return (float(arguments_right_result) + float(prefixScore(d)))/2.0
    return sys.maxint
def argumentsRight(d):
    args = ["FromExaminationName","ToExaminationName","RigidTransformation","RotationCenter","RollDegrees","PitchDegrees","YawDegrees","Translation"]
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
    score_temp = lib.score_generic(d, "SetRigidTransformation")
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
    return json.loads("{\"base\": \"Patient.Cases.[]\", \"params\": [\"FromExaminationName\", \"ToExaminationName\", \"RigidTransformation\", \"RotationCenter\", \"RollDegrees\", \"PitchDegrees\", \"YawDegrees\", \"Translation\"], \"method\": \"SetRigidTransformation\", \"description\": \"SetRigidTransformation(..)\\r\\n  Sets the rigid transformation between two examinations.\\r\\n  Parameters:\\r\\n    FromExaminationName - The name of the from examination \\r\\n      that defines the from frame of reference.\\r\\n    ToExaminationName - The name of the to examination that \\r\\n      defines the to frame of reference.\\r\\n    RigidTransformation - The rigid transformation. Defined by \\r\\n      three rotation angles, a rotation center, and a translation.\\r\\n        RotationCenter - The pivot point for rotations [cm]. In \\r\\n      DICOM coordinates.\\r\\n        RollDegrees - Rotation about the Inferior-Superios axis \\r\\n      (DICOM: z, IEC: y).\\r\\n        PitchDegrees - Rotation about the Right-Left axis (DICOM: x, \\r\\n      IEC: x).\\r\\n        YawDegrees - Rotation about the Posterior-Anterior axis \\r\\n      (DICOM: -y, IEC: z).\\r\\n        Translation - The translation [cm]. In DICOM coordinates.\\r\\n                  \\r\\n      Example:\\r\\n        RigidTransformation = \\r\\n        { \\r\\n          'YawDegrees': 0.5, \\r\\n          'PitchDegrees': -3.1, \\r\\n          'RollDegrees': 7.32, \\r\\n          'Translation': { 'x': 1.1, 'y': -3.2, 'z': 2.8 }, \\r\\n          'RotationCenter': { 'x': 0, 'y': 0, 'z': 0 } \\r\\n        }\\r\\n                  \\r\\n      The order of transformations is \\r\\n        (1) negative rotation center shift\\r\\n        (2) yaw rotation about posterior-anterior axis\\r\\n        (3) pitch rotation about right-left axis,\\r\\n        (4) roll rotation about inferior-superior axis,\\r\\n        (5) positive rotation center shift\\r\\n        (6) translation\\r\\n                  \\r\\n      The matrix representing the rigid transformation is\\r\\n                  \\r\\n        M = T * Tc * R_roll * R_pitch * R_yaw * T-c, \\r\\n                  \\r\\n      where T is a translation matrix representing Translation, Tc \\r\\n      and T-c are translation matrices \\r\\n      representing rotation center shifts, and R_roll, R_pitch, and \\r\\n      R_yaw are rotation matrices \\r\\n      representing the respective rotations.\\r\\n\"}")
