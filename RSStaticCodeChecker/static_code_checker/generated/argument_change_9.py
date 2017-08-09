import lib.lib as lib
import json
def easyCheck(s):
    return "ImportDeformableRegistrationFromMetaImageFile" in s
def scoreForDict(d):
    import sys
    if not isinstance(d, dict):
        return sys.maxint
    arguments_right_result = argumentsRight(d)
    if arguments_right_result != True:
        return (float(arguments_right_result) + float(prefixScore(d)))/2.0
    return sys.maxint
def argumentsRight(d):
    args = ["ReferenceExaminationName","TargetExaminationName","DeformableRegistrationGroupName","RigidTransform","MetaImageHeaderFileName"]
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
    score_temp = lib.score_generic(d, "ImportDeformableRegistrationFromMetaImageFile")
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
    return json.loads("{\"base\": \"Patient.Cases.[]\", \"params\": [\"ReferenceExaminationName\", \"TargetExaminationName\", \"DeformableRegistrationGroupName\", \"RigidTransform\", \"MetaImageHeaderFileName\"], \"method\": \"ImportDeformableRegistrationFromMetaImageFile\", \"description\": \"ImportDeformableRegistrationFromMetaImageFile(..)\\r\\n  Action for reading a deformable registration stored as a meta \\r\\n  image file.\\r\\n  Assumes that all units are mm (corner, grid element size and \\r\\n  displacement)\\r\\n  Displacement field should be stored as float (ELEMENT_TYPE = \\r\\n  MET_FLOAT in header file)\\r\\n  Parameters:\\r\\n    ReferenceExaminationName - Gets or sets the name of the \\r\\n      reference examination.\\r\\n    TargetExaminationName - Gets or sets the name of the \\r\\n      target examination.\\r\\n    DeformableRegistrationGroupName - Gets or sets the name of \\r\\n      the deformable registration group that will be created.\\r\\n    RigidTransform - Gets or sets the rigid transform for the \\r\\n      deformable registration.\\r\\n      If null, the identity matrix will be assumed.\\r\\n      In RayStation, two frame-of-references have a unique \\r\\n      registration, meaning there is only support for one \\r\\n      frame-of-reference registration between two image sets. \\r\\n      In addition to the frame-of-reference registration an \\r\\n      additional rigid transform can be created and stored (below \\r\\n      refered to as \\\"added rigid transform\\\"). \\r\\n      The combination of the frame-of-reference registration and the \\r\\n      added rigid transform will be the starting point for the \\r\\n      deformable registration. \\r\\n      This means that the parameter \\\"RigidTransform\\\" need to fulfil \\r\\n      one of the following:If the reference image and the target \\r\\n      image are already rigidly registered in RayStation the \\r\\n      transform need to fulfil:\\r\\n      1. no frame-of-reference registration exists between reference \\r\\n      and target\\r\\n          -> frame-of-reference registration will be set to \\r\\n      \\\"RigidTransform\\\" and added rigid transform to identity \\r\\n      2. identical to the frame-of-reference registration between \\r\\n      reference and target AND no added rigid transform between the \\r\\n      image set exists\\r\\n          -> added rigid transform will be set to identity \\r\\n      3. identical to the combined frame-of-reference registration \\r\\n      and added rigid transform between the image sets\\r\\n      4. difference than the frame-of-reference registration between \\r\\n      reference and target AND no added rigid transform exists\\r\\n          -> added rigid transform will be set to the difference \\r\\n      between the frame-of-reference registration and \\\"RigidTransform\\\"\\r\\n      Independently of the situation, no added rigid transform can \\r\\n      be added once the action is finished (as only one can exist \\r\\n      between the same set of images)\\r\\n                  \\r\\n      If RigidTransform is empty, existing transform will be used.\\r\\n    MetaImageHeaderFileName - Gets or sets the file name for \\r\\n      the meta file in which the displacement field is given.\\r\\n\"}")
