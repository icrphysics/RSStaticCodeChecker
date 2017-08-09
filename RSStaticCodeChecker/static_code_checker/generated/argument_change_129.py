import lib.lib as lib
import json
def easyCheck(s):
    return "ImageSimilarityForRigidRegistration" in s
def scoreForDict(d):
    import sys
    if not isinstance(d, dict):
        return sys.maxint
    arguments_right_result = argumentsRight(d)
    if arguments_right_result != True:
        return (float(arguments_right_result) + float(prefixScore(d)))/2.0
    return sys.maxint
def argumentsRight(d):
    args = ["ReferenceImageName","TargetImageName","RigidTransformation","RoiNames"]
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
    score_temp = lib.score_generic(d, "ImageSimilarityForRigidRegistration")
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
    return json.loads("{\"base\": \"Patient.Cases.[]\", \"params\": [\"ReferenceImageName\", \"TargetImageName\", \"RigidTransformation\", \"RoiNames\"], \"method\": \"ImageSimilarityForRigidRegistration\", \"description\": \"ImageSimilarityForRigidRegistration(..)\\r\\n  Compute image similarity between two images (reference and \\r\\n  target). A rigid transformation is applied to the reference image. \\r\\n  Use Patient.GetTransformForExaminations() with FromExamination as \\r\\n  reference and ToExamination as target to \\r\\n  get the transform corresponding to the frame-of-reference \\r\\n  registration.\\r\\n              \\r\\n  Only voxels inside the selected rois on the reference image are \\r\\n  considered. If no rois are selected, external geometry will be used\\r\\n   (i.e., consistent with rigid image registration algorithm)\\r\\n  Parameters:\\r\\n    ReferenceImageName - Name of the reference image. The \\r\\n      rigid transformation will be applied to this image.\\r\\n    TargetImageName - Name of the target image.\\r\\n    RigidTransformation - Rigid transformation as a double \\r\\n      array.\\r\\n    RoiNames - Names of the rois over which you want to \\r\\n      compute image similarity. If left empty the external geometry \\r\\n      will be used\\r\\n  Returns:\\r\\n    A dictionary with 'CorrelationCoefficient'\\r\\n\"}")
