import lib.lib as lib
import json
def easyCheck(s):
    return "SetTreatmentPositionAlignmentRegistration" in s
def scoreForDict(d):
    import sys
    if not isinstance(d, dict):
        return sys.maxint
    arguments_right_result = argumentsRight(d)
    if arguments_right_result != True:
        return (float(arguments_right_result) + float(prefixScore(d)))/2.0
    return sys.maxint
def argumentsRight(d):
    args = ["ManualTPAlignment","SetupCorrectionIncludedInCbctIsocenter","CouchRotationAngle","CouchRotationAxis","CouchTranslation","IsocenterReference","IntrinsicIsocenter","TreatmentPlanForDelivery"]
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
    from bases import score_Examination
    steps += 1
    score_temp = lib.score_generic(d, "SetTreatmentPositionAlignmentRegistration")
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    steps += 1
    score_temp = score_Examination.get_score(d.get("value"))
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    return float(score) / float(steps)
def get_info():
    return json.loads("{\"base\": \"Examination\", \"params\": [\"ManualTPAlignment\", \"SetupCorrectionIncludedInCbctIsocenter\", \"CouchRotationAngle\", \"CouchRotationAxis\", \"CouchTranslation\", \"IsocenterReference\", \"IntrinsicIsocenter\", \"TreatmentPlanForDelivery\"], \"method\": \"SetTreatmentPositionAlignmentRegistration\", \"description\": \"SetTreatmentPositionAlignmentRegistration(..)\\r\\n  Action that sets treatment position alignment registration for a \\r\\n  CBCT image to the planning image for the treatment delivery plan.\\r\\n  The CBCT image will be aligned with respect to the beam isocenter \\r\\n  of the beams for the current fraction. \\r\\n  Treatment adaptation has to be initialized.\\r\\n              \\r\\n  Example 1, Manually entered isocenter, Setup correction included \\r\\n  in CBCT isocenter:\\r\\n  case.Examinations['CBCT \\r\\n  4'].SetTreatmentPositionAlignmentRegistration(ManualTPAlignment=True, SetupCorrectionIncludedInCbctIsocenter=True, IsocenterReference=\\\"Intrinsic\\\", IntrinsicIsocenter={ 'x': -22.44, 'y': -22.44, 'z': -0.17 }, TreatmentPlanForDelivery=plan) \\r\\n  \\r\\n              \\r\\n  Example 2, Isocenter from treatment plan, Manually entered couch \\r\\n  setup:\\r\\n  case.Examinations['CBCT \\r\\n  4'].SetTreatmentPositionAlignmentRegistration(ManualTPAlignment=True, SetupCorrectionIncludedInCbctIsocenter=False, CouchRotationAngle=358, CouchRotationAxis={ 'x': 0, 'y': -1, 'z': 0 }, CouchTranslation={ 'x': 1, 'y': -1.5, 'z': 0.5 }, IsocenterReference=\\\"RtPlan\\\", TreatmentPlanForDelivery=plan)\\r\\n  \\r\\n              \\r\\n  Example 3, Varian OBI imaging system with marker match POIs:\\r\\n  case.Examinations['CBCT \\r\\n  4'].SetTreatmentPositionAlignmentRegistration(ManualTPAlignment=False, SetupCorrectionIncludedInCbctIsocenter=False, CouchRotationAngle=0, CouchRotationAxis={ 'x': 0, 'y': -1, 'z': 0 }, CouchTranslation={ 'x': 0.15, 'y': 0.16, 'z': -0.16 }, IsocenterReference=\\\"Intrinsic\\\", IntrinsicIsocenter={ 'x': -23.42, 'y': -24.21, 'z': 0.1 }, TreatmentPlanForDelivery=plan)\\r\\n  \\r\\n  Intrisic isocenter is the position of the Aquisition isocenter POI \\r\\n  on the CBCT.\\r\\n  The couch translation is calculated as the Aquisition isocenter \\r\\n  POI - Initial match isocenter POI on the CBCT.\\r\\n  Parameters:\\r\\n    ManualTPAlignment - Defines if the treatment position \\r\\n      alignment information is given manually. (In opposite to if \\r\\n      marker match POIs is used, supported only by Varian OBI)\\r\\n    SetupCorrectionIncludedInCbctIsocenter - Defines if setup \\r\\n      correction is included in cbct isocenter information or not. \\r\\n      If not, couch rotation angle, couch rotation axis and couch \\r\\n      translation need to be defined.\\r\\n      Otherwise, those parameters should be set to null\\r\\n    CouchRotationAngle - Setup correction: couch rotation \\r\\n      angle [deg]\\r\\n    CouchRotationAxis - Setup correction: couch rotation axis \\r\\n      (in DICOM coordinates). Needs to be of length one. \\r\\n      Default from UI is rotation around Post-Ant direction, i.e., \\r\\n      {'x': 0, 'y': -1, 'z': 0} when used from scripting (dicom \\r\\n      coordinates)\\r\\n    CouchTranslation - Setup correction: couch translation [cm].\\r\\n    IsocenterReference - How the coordinate system of the CBCT \\r\\n      image is defined. Possible values:\\r\\n      'Intrinsic'  : Coordinate system for which the isocenter point \\r\\n      used during patient setup has the coordinates of the \\r\\n      IntrinsicIsocenter\\r\\n      'RtPlan'     : Coordinate system for which the isocenter point \\r\\n      used during patient setup has the coordinates as in the \\r\\n      corresponding plan, i.e., the image is pre-aligned with the \\r\\n      frame-of-reference used in the plan\\r\\n    IntrinsicIsocenter - Coordinate corresponding to the \\r\\n      isocenter of the CBCT image [cm]\\r\\n      Required if 'IsocenterReference' is 'Intrinsic'. \\r\\n      In case 'IsocenterReference' is 'RtPlan', 'IntrinsicIsocenter' \\r\\n      will be set to the (shared) beam isocenter for the radiation \\r\\n      set used for the current fraction.\\r\\n    TreatmentPlanForDelivery - Plan used for treatment delivery\\r\\n\"}")
