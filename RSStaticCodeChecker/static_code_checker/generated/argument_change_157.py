import lib.lib as lib
import json
def easyCheck(s):
    return "AddNewAdaptivePlan" in s
def scoreForDict(d):
    import sys
    if not isinstance(d, dict):
        return sys.maxint
    arguments_right_result = argumentsRight(d)
    if arguments_right_result != True:
        return (float(arguments_right_result) + float(prefixScore(d)))/2.0
    return sys.maxint
def argumentsRight(d):
    args = ["FractionNumber","AdaptToPlanName","UseTreatmentDeliveryAsSource","PlanName","PlannedBy","Comment","ExaminationName","AllowDuplicateNames"]
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
    score_temp = lib.score_generic(d, "AddNewAdaptivePlan")
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
    return json.loads("{\"base\": \"Patient.Cases.[]\", \"params\": [\"FractionNumber\", \"AdaptToPlanName\", \"UseTreatmentDeliveryAsSource\", \"PlanName\", \"PlannedBy\", \"Comment\", \"ExaminationName\", \"AllowDuplicateNames\"], \"method\": \"AddNewAdaptivePlan\", \"description\": \"AddNewAdaptivePlan(..)\\r\\n  Action for creating a new adapted plan.\\r\\n              \\r\\n  Prerequisite: deformable image registration (DIR) with new \\r\\n  planning image as reference image and original planning image as \\r\\n  target image. \\r\\n  The DIR should be approved for dose accumulation.\\r\\n              \\r\\n  Example:\\r\\n  # add new adapted plan from fraction 10 to a plan with one beam \\r\\n  set using planning image \\\"RESCAN\\\"\\r\\n  patient = get_current(\\\"Patient\\\")\\r\\n  case = get_current(\\\"Case\\\")\\r\\n  plan=get_current(\\\"Plan\\\")\\r\\n  beam_set=get_current(\\\"BeamSet\\\")\\r\\n  adapt_from_fx = 10\\r\\n  adapted_ct = \\\"RESCAN\\\"\\r\\n  tot_nr_fx = len([tf for tf in \\r\\n  plan.TreatmentCourse.TreatmentFractions])\\r\\n              \\r\\n  adapted_plan = case.AddNewAdaptivePlan(FractionNumber= \\r\\n  adapt_from_fx, AdaptToPlanName= plan.Name, \\r\\n  UseTreatmentDeliveryAsSource= True,\\r\\n  PlanName= \\\"Adapted plan\\\", PlannedBy= None, Comment= \\\"\\\", \\r\\n  ExaminationName= adapted_ct, AllowDuplicateNames= False)\\r\\n  treatment_technique = beam_set.GetTreatmentTechniqueType()\\r\\n              \\r\\n  beam_set_settings = {'NumberOfRemainingFractions': tot_nr_fx - \\r\\n  adapt_from_fx, 'MachineName': \\r\\n  beam_set.MachineReference.MachineName, \\r\\n  'CreateSetupBeams': true, 'DicomPlanLabelOfOriginalBeamSet': \\r\\n  beam_set.DicomPlanLabel, 'ClearBeamModifiers': false, \\r\\n  'RemoveBeams': false, 'TreatmentTechnique': treatment_technique}\\r\\n  adapted_plan.AddBeamSetsToAdaptedPlan(AdaptedBeamSets=[beam_set_settings])\\r\\n  \\r\\n  adapted_beam_set = adapted_plan.BeamSets[0]\\r\\n  prescription = beam_set.Prescription.PrimaryDosePrescription\\r\\n  adapted_beam_set.AddDosePrescriptionToRoi(\\r\\n  RoiName=prescription.OnStructure.Name,\\r\\n  DoseVolume=prescription.DoseVolume,\\r\\n  PrescriptionType=prescription.PrescriptionType,\\r\\n  DoseValue=prescription.DoseValue,\\r\\n  RelativePrescriptionLevel=prescription.RelativePrescriptionLevel,\\r\\n  AutoScaleDose=False)\\r\\n  Parameters:\\r\\n    FractionNumber - Fraction for which to start the delivery \\r\\n      of the adapted plan. \\r\\n      FractionNumber has to be less or equal to the number of \\r\\n      fractions for the original plan + 1.\\r\\n      If 'UseTreatmentDeliveryAsSource', FractionNumber needs to be \\r\\n      larger than the number of delivered fractions\\r\\n    AdaptToPlanName - Name of the plan for which adaptation \\r\\n      should be done\\r\\n    UseTreatmentDeliveryAsSource - Sets if background dose \\r\\n      during optimization should be \\r\\n      - delivered accumulated dose (as computed in DoseTracking \\r\\n      workspace and store as TreatmentCourse under \\r\\n      TreatmentDelivery) [TRUE], or\\r\\n      - planned accumulated dose [FALSE]\\r\\n    PlanName - Name of the new plan.\\r\\n    PlannedBy - Name of the planner.\\r\\n    Comment - Comments of the new plan.\\r\\n    ExaminationName - The name of the planning image set \\r\\n      defined for the new plan\\r\\n    AllowDuplicateNames - Skip uniqueness test for name (used \\r\\n      by fallback plans).\\r\\n\"}")
