import lib.lib as lib
import json
def easyCheck(s):
    return "CreateHybridDeformableRegistrationGroup" in s
def scoreForDict(d):
    import sys
    if not isinstance(d, dict):
        return sys.maxint
    arguments_right_result = argumentsRight(d)
    if arguments_right_result != True:
        return (float(arguments_right_result) + float(prefixScore(d)))/2.0
    return sys.maxint
def argumentsRight(d):
    args = ["RegistrationGroupName","ReferenceExaminationName","TargetExaminationNames","ControllingRoiNames","ControllingPoiNames","FocusRoiNames","AlgorithmSettings"]
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
    score_temp = lib.score_generic(d, "CreateHybridDeformableRegistrationGroup")
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    steps += 1
    score_temp = lib.score_generic(d.get("value"), "PatientModel")
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
    score_temp = lib.score_generic(d.get("value").get("value").get("value"), "Cases")
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    steps += 1
    score_temp = score_Patient.get_score(d.get("value").get("value").get("value").get("value"))
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    return float(score) / float(steps)
def get_info():
    return json.loads("{\"base\": \"Patient.Cases.[].PatientModel\", \"params\": [\"RegistrationGroupName\", \"ReferenceExaminationName\", \"TargetExaminationNames\", \"ControllingRoiNames\", \"ControllingPoiNames\", \"FocusRoiNames\", \"AlgorithmSettings\"], \"method\": \"CreateHybridDeformableRegistrationGroup\", \"description\": \"CreateHybridDeformableRegistrationGroup(..)\\r\\n  Creates a deformable registration group with hybrid deformable \\r\\n  registrations for the selected reference examination and target \\r\\n  examinations.\\r\\n  Parameters:\\r\\n    RegistrationGroupName - A registration group with this \\r\\n      name is created.\\r\\n    ReferenceExaminationName - The examination where the \\r\\n      deformation field is defined.\\r\\n    TargetExaminationNames - The examinations the deformation \\r\\n      fields will point to.\\r\\n    ControllingRoiNames - The list with ROI names for the \\r\\n      controlling ROIs.\\r\\n    ControllingPoiNames - The list with POI names for the \\r\\n      controlling POIs.\\r\\n    FocusRoiNames - The list with ROI names for the focus ROIs.\\r\\n    AlgorithmSettings - The algorithm settings.\\r\\n                  \\r\\n      Properties:\\r\\n                  \\r\\n        * NumberOfResolutionLevels\\r\\n          The number of resolution levels.\\r\\n        * InitialResolution\\r\\n          The deformation grid resolution (cm) at the initial \\r\\n      resolution level given in the DICOM patient-based coordinate \\r\\n      system. \\r\\n          Typical value (0.5, 0.5, 0.5).\\r\\n        * FinalResolution\\r\\n          The deformation grid resolution (cm) at the final \\r\\n      resolution level given in the DICOM patient-based coordinate \\r\\n      system. \\r\\n          Typical value (0.25, 0.25, 0.25).\\r\\n        * InitialGaussianSmoothingSigma\\r\\n          The Gaussian smoothing sigma at the initial resolution \\r\\n      level. Typical value 2.0.\\r\\n        * FinalGaussianSmoothingSigma\\r\\n          The Gaussian smoothing sigma at the final resolution \\r\\n      level. Typical value 0.333.\\r\\n        * InitialGridRegularizationWeight\\r\\n          The grid regularization weight at the initial resolution \\r\\n      level. Typical value 1500.0.\\r\\n        * FinalGridRegularizationWeight\\r\\n          The grid regularization weight at the final resolution \\r\\n      level. Typical value 400.0.\\r\\n        * ControllingRoiWeight\\r\\n          The controlling ROI weight. Typical value 0.5.\\r\\n        * ControllingPoiWeight\\r\\n          The controlling POI weight. Typical value 0.1.\\r\\n        * MaxNumberOfIterationsPerResolutionLevel\\r\\n          The maximum number of iterations per resolution level. \\r\\n      Typical value 1000.\\r\\n        * ImageSimilarityMeasure\\r\\n          The image similarity measure. Possible values: \\r\\n      \\\"CorrelationCoefficient\\\", \\\"MutualInformation\\\", \\r\\n      \\\"MixedCorrelationMutual\\\", \\\"None\\\".\\r\\n        * DeformationStrategy. Possible values: \\\"Default\\\", \\r\\n      \\\"InternalLung\\\".\\r\\n        * ConvergenceTolerance\\r\\n          The tolerance for convergence. Typical value 1e-5.\\r\\n      Example: \\r\\n                  \\r\\n        AlgorithmSettings = \\r\\n        {\\r\\n          'NumberOfResolutionLevels': 3,\\r\\n          'InitialResolution': { 'x': 0.5, 'y': 0.5, 'z': 0.5 },\\r\\n          'FinalResolution': { 'x': 0.25, 'y': 0.25, 'z': 0.25 },\\r\\n          'InitialGaussianSmoothingSigma': 2.0,\\r\\n          'FinalGaussianSmoothingSigma': 0.333,\\r\\n          'InitialGridRegularizationWeight': 1500.0,\\r\\n          'FinalGridRegularizationWeight': 400.0,\\r\\n          'ControllingRoiWeight': 0.5,\\r\\n          'ControllingPoiWeight': 0.1,\\r\\n          'MaxNumberOfIterationsPerResolutionLevel': 1000, \\r\\n          'ImageSimilarityMeasure': \\\"CorrelationCoefficient\\\",\\r\\n          'DeformationStrategy': \\\"DeformationStrategy\\\",\\r\\n          'ConvergenceTolerance': 1e-5\\r\\n        }\\r\\n\"}")
