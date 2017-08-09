import lib.lib as lib
import json
def easyCheck(s):
    return "AddBeamSetsToAdaptedPlan" in s
def scoreForDict(d):
    import sys
    if not isinstance(d, dict):
        return sys.maxint
    arguments_right_result = argumentsRight(d)
    if arguments_right_result != True:
        return (float(arguments_right_result) + float(prefixScore(d)))/2.0
    return sys.maxint
def argumentsRight(d):
    args = ["AdaptedBeamSets","NumberOfRemainingFractions","MachineName","CreateSetupBeams","ClearBeamModifiers","RemoveBeams","NOTE"]
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
    score_temp = lib.score_generic(d, "AddBeamSetsToAdaptedPlan")
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
    score_temp = lib.score_generic(d.get("value").get("value"), "TreatmentPlans")
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    steps += 1
    score_temp = score_Case.get_score(d.get("value").get("value").get("value"))
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    return float(score) / float(steps)
def get_info():
    return json.loads("{\"base\": \"Case.TreatmentPlans.[]\", \"params\": [\"AdaptedBeamSets\", \"NumberOfRemainingFractions\", \"MachineName\", \"CreateSetupBeams\", \"ClearBeamModifiers\", \"RemoveBeams\", \"NOTE\"], \"method\": \"AddBeamSetsToAdaptedPlan\", \"description\": \"AddBeamSetsToAdaptedPlan(..)\\r\\n  Action for adding beamsets to an adapted plan.\\r\\n  Prerequisite:\\r\\n    Can only be used on adapted plans with no beam set(s)\\r\\n              \\r\\n  Example:\\r\\n  # add new adapted plan from fraction 10 to a plan with one beam \\r\\n  set using planning image \\\"RESCAN\\\"\\r\\n  patient = get_current(\\\"Patient\\\")\\r\\n  case = get_current(\\\"Case\\\")\\r\\n  plan=get_current(\\\"Plan\\\")\\r\\n  beam_set=get_current(\\\"BeamSet\\\")\\r\\n  adapt_from_fx = 10\\r\\n  adapted_ct = \\\"RESCAN\\\"\\r\\n  tot_nr_fx = len([tf for tf in \\r\\n  plan.TreatmentCourse.TreatmentFractions])\\r\\n              \\r\\n  adapted_plan = case.AddNewAdaptivePlan(FractionNumber= \\r\\n  adapt_from_fx, AdaptToPlanName= plan.Name, \\r\\n  UseTreatmentDeliveryAsSource= True,\\r\\n  PlanName= \\\"Adapted plan\\\", PlannedBy= None, Comment= \\\"\\\", \\r\\n  ExaminationName= adapted_ct, AllowDuplicateNames= False)\\r\\n  treatment_technique = beam_set.GetTreatmentTechniqueType()\\r\\n              \\r\\n  beam_set_settings = {'NumberOfRemainingFractions': tot_nr_fx - \\r\\n  adapt_from_fx, 'MachineName': \\r\\n  beam_set.MachineReference.MachineName, \\r\\n  'CreateSetupBeams': true, 'DicomPlanLabelOfOriginalBeamSet': \\r\\n  beam_set.DicomPlanLabel, 'ClearBeamModifiers': false, \\r\\n  'RemoveBeams': false, 'TreatmentTechnique': treatment_technique}\\r\\n  adapted_plan.AddBeamSetsToAdaptedPlan(AdaptedBeamSets=[beam_set_settings])\\r\\n  \\r\\n  adapted_beam_set = adapted_plan.BeamSets[0]\\r\\n  prescription = beam_set.Prescription.PrimaryDosePrescription\\r\\n  adapted_beam_set.AddDosePrescriptionToRoi(\\r\\n  RoiName=prescription.OnStructure.Name,\\r\\n  DoseVolume=prescription.DoseVolume,\\r\\n  PrescriptionType=prescription.PrescriptionType,\\r\\n  DoseValue=prescription.DoseValue,\\r\\n  RelativePrescriptionLevel=prescription.RelativePrescriptionLevel,\\r\\n  AutoScaleDose=False)\\r\\n  Parameters:\\r\\n    AdaptedBeamSets - List of AdaptedBeamSetSettings\\r\\n      Settings is stored as a dictionary on form \\r\\n      \\\"NumberOfRemainingFractions\\\", \\\"MachineName\\\",\\r\\n      \\\"CreateSetupBeams\\\", \\\"DicomPlanLabelOfOriginalBeamSet\\\",\\r\\n      \\\"ClearBeamModifiers\\\", \\\"RemoveBeams\\\", \\\"TreatmentTechnique\\\"\\r\\n                  \\r\\n      NumberOfRemainingFractions - Number of remaining fractions.\\r\\n      MachineName - Name of the machine. The last commissioned \\r\\n      machine in the database will be used.\\r\\n      CreateSetupBeams - Set to true if setupbeams shall be created.\\r\\n      ClearBeamModifiers - Set to true if beam contents shall be \\r\\n      cleared.\\r\\n      RemoveBeams - Set to true if all beams should be removed.\\r\\n      NOTE - If both RemoveBeams and ClearBeamModifiers are true, \\r\\n      beams will be removed. If both are false nothing will be done.\\r\\n\"}")
