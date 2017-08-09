import lib.lib as lib
import json
def easyCheck(s):
    return "CreateNewDeformableRegistration" in s
def scoreForDict(d):
    import sys
    if not isinstance(d, dict):
        return sys.maxint
    arguments_right_result = argumentsRight(d)
    if arguments_right_result != True:
        return (float(arguments_right_result) + float(prefixScore(d)))/2.0
    return sys.maxint
def argumentsRight(d):
    args = ["ReferenceExaminationName","TargetExaminationName","RegistrationName","RigidTransformDF","RigidTransformFoR","FromFrameOfReference","ToFrameOfReference","GridCorner","GridVoxelSize","NrOfVoxels","DisplacementField"]
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
    score_temp = lib.score_generic(d, "CreateNewDeformableRegistration")
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
    return json.loads("{\"base\": \"Patient.Cases.[]\", \"params\": [\"ReferenceExaminationName\", \"TargetExaminationName\", \"RegistrationName\", \"RigidTransformDF\", \"RigidTransformFoR\", \"FromFrameOfReference\", \"ToFrameOfReference\", \"GridCorner\", \"GridVoxelSize\", \"NrOfVoxels\", \"DisplacementField\"], \"method\": \"CreateNewDeformableRegistration\", \"description\": \"CreateNewDeformableRegistration(..)\\r\\n  Action for adding a new deformable registration based on \\r\\n  information stored in files. Used from scripting (see \\r\\n  Dev01\\\\CoreApps\\\\ScriptClient\\\\InternalScripts\\\\import_deformableregistration.py).\\r\\n  Parameters:\\r\\n    ReferenceExaminationName - Gets or sets the name of the \\r\\n      reference examination.\\r\\n    TargetExaminationName - Gets or sets the name of the \\r\\n      target examination.\\r\\n    RegistrationName - Gets or sets the name of the structure \\r\\n      registration.\\r\\n    RigidTransformDF - Gets or sets the rigid transform for \\r\\n      the deformable registration.\\r\\n    RigidTransformFoR - Gets or sets the rigid transform for \\r\\n      the frame-of-reference registration.\\r\\n    FromFrameOfReference - Gets or sets the the from \\r\\n      frame-of-reference\\r\\n    ToFrameOfReference - Gets or sets the the to \\r\\n      frame-of-reference\\r\\n    GridCorner - Gets or sets the deformation grid corner.\\r\\n    GridVoxelSize - Gets or sets the deformation grid voxel \\r\\n      size.\\r\\n    NrOfVoxels - Gets or sets the deformation grid size.\\r\\n    DisplacementField - Gets or sets the displacement field.\\r\\n\"}")
