import lib.lib as lib
import json
def easyCheck(s):
    return "ImportDeformableRegistrationFromFile" in s
def scoreForDict(d):
    import sys
    if not isinstance(d, dict):
        return sys.maxint
    arguments_right_result = argumentsRight(d)
    if arguments_right_result != True:
        return (float(arguments_right_result) + float(prefixScore(d)))/2.0
    return sys.maxint
def argumentsRight(d):
    args = ["ReferenceExaminationName","TargetExaminationName","DeformableRegistrationGroupName","AddedRigidTransform","FrameOfReferenceRigidTransform","GridCorner","GridVoxelSize","GridNrVoxels","FileNameDisplacementX","FileNameDisplacementY","FileNameDisplacementZ"]
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
    score_temp = lib.score_generic(d, "ImportDeformableRegistrationFromFile")
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
    return json.loads("{\"base\": \"Case\", \"params\": [\"ReferenceExaminationName\", \"TargetExaminationName\", \"DeformableRegistrationGroupName\", \"AddedRigidTransform\", \"FrameOfReferenceRigidTransform\", \"GridCorner\", \"GridVoxelSize\", \"GridNrVoxels\", \"FileNameDisplacementX\", \"FileNameDisplacementY\", \"FileNameDisplacementZ\"], \"method\": \"ImportDeformableRegistrationFromFile\", \"description\": \"ImportDeformableRegistrationFromFile(..)\\r\\n  Action for reading a deformable registration from file.\\r\\n  Displacement in x, y, and z should be stored as byte arrays\\r\\n  Parameters:\\r\\n    ReferenceExaminationName - Gets or sets the name of the \\r\\n      reference examination.\\r\\n    TargetExaminationName - Gets or sets the name of the \\r\\n      target examination.\\r\\n    DeformableRegistrationGroupName - Gets or sets the name of \\r\\n      the deformable registration group that will be created.\\r\\n    AddedRigidTransform - Gets or sets the rigid transform for \\r\\n      the deformable registration.\\r\\n      If null, the identity matrix will be used.\\r\\n      Note that in RayStation only one additional rigid transform \\r\\n      can be added between each pair of image set. \\r\\n      This means that if you have already created an additional \\r\\n      rigid transform, the same matrix should be given as \\r\\n      AddedRigidTransform\\r\\n      Furthermore, rigid transforms (if different than identity) can \\r\\n      only be added to explicit frame-of-reference registrations\\r\\n    FrameOfReferenceRigidTransform - Gets or sets the rigid \\r\\n      transform for the frame-of-reference registration.\\r\\n      If a frame-of-reference registration already exist between the \\r\\n      reference and target examination, \\r\\n      FrameOfReferenceRigidTransform should be null\\r\\n    GridCorner - Gets or sets the deformation grid corner.\\r\\n      Note that deformation vectors are defined in the corner points \\r\\n      of each deformation grid voxels. Hence, GridCorner should \\r\\n      correspond to position of the first deformation vector in your \\r\\n      deformation vector field\\r\\n    GridVoxelSize - Gets or sets the deformation grid voxel \\r\\n      size.\\r\\n    GridNrVoxels - Gets or sets the deformation grid size.\\r\\n      Note that deformation vectors are defined in the corner points \\r\\n      of each deformation grid voxels. Hence, GridNrVoxels should be \\r\\n      decreased with one in each direction with respect to the \\r\\n      number of vectors\\r\\n    FileNameDisplacementX - Gets or sets the file name for \\r\\n      displacement field in x.\\r\\n    FileNameDisplacementY - Gets or sets the file name for \\r\\n      displacement field in y.\\r\\n    FileNameDisplacementZ - Gets or sets the file name for \\r\\n      displacement field in z.\\r\\n\"}")
