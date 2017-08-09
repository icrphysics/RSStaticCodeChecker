import lib.lib as lib
import json
def easyCheck(s):
    return "ScriptableDicomExport" in s
def scoreForDict(d):
    import sys
    if not isinstance(d, dict):
        return sys.maxint
    arguments_right_result = argumentsRight(d)
    if arguments_right_result != True:
        return (float(arguments_right_result) + float(prefixScore(d)))/2.0
    return sys.maxint
def argumentsRight(d):
    args = ["Anonymize","AnonymizedName","AnonymizedId","ExportFolderPath","AEHostname","AEPort","CallingAETitle","CalledAETitle","Examinations","RtStructureSetsForExaminations","RtStructureSetsReferencedFromBeamSets","BeamSets","BeamSetDoseForBeamSets","BeamDosesForBeamSets","SpatialRegistrationForExaminations","TreatmentBeamDrrImages","SetupBeamDrrImages","DicomFilter","IgnorePreConditionWarnings","Useatry"]
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
    score_temp = lib.score_generic(d, "ScriptableDicomExport")
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
    return json.loads("{\"base\": \"Case\", \"params\": [\"Anonymize\", \"AnonymizedName\", \"AnonymizedId\", \"ExportFolderPath\", \"AEHostname\", \"AEPort\", \"CallingAETitle\", \"CalledAETitle\", \"Examinations\", \"RtStructureSetsForExaminations\", \"RtStructureSetsReferencedFromBeamSets\", \"BeamSets\", \"BeamSetDoseForBeamSets\", \"BeamDosesForBeamSets\", \"SpatialRegistrationForExaminations\", \"TreatmentBeamDrrImages\", \"SetupBeamDrrImages\", \"DicomFilter\", \"IgnorePreConditionWarnings\", \"Useatry\"], \"method\": \"ScriptableDicomExport\", \"description\": \"ScriptableDicomExport(..)\\r\\n  Exports specified DICOM datasets to either disk or SCP.\\r\\n  Parameters:\\r\\n    Anonymize - Anonymize all exported datasets\\r\\n    AnonymizedName - Patients name to set in anonymized datasets\\r\\n    AnonymizedId - Patient ID to set in anonymized datasets\\r\\n    ExportFolderPath - Export target folder. Only used for \\r\\n      file exports. Leave empty for SCP export\\r\\n    AEHostname - SCP AE name for SCP export. Leave empty for \\r\\n      file export\\r\\n    AEPort - SCP Port for SCP export. Leave empty for file \\r\\n      export\\r\\n    CallingAETitle - Calling AE title for SCP export. Leave \\r\\n      empty to use hostname\\r\\n    CalledAETitle - Called AE title for SCP export\\r\\n    Examinations - List of examination that shall be exported. \\r\\n      Specified by Examination names\\r\\n      Argument snippet: Examinations = [examination.Name]\\r\\n    RtStructureSetsForExaminations - List of examination names \\r\\n      for which the structure set shall be exported.\\r\\n      Specified by examination names\\r\\n      Argument snippet: RtStructureSetsForExaminations = \\r\\n      [examination.Name]\\r\\n    RtStructureSetsReferencedFromBeamSets - List of beamset \\r\\n      identifiers for which the referenced structure set that shall \\r\\n      be exported\\r\\n      The identifier shall be specified as PlanName:DicomPlanLabel \\r\\n      (ex. \\\"Plan 1:BS 1\\\" for plan \\\"Plan 1\\\" with beam set \\\"BS 1\\\")\\r\\n      Argument snippet: RtStructureSetsReferencedFromBeamSets = \\r\\n      [\\\"%s:%s\\\"%(plan.Name, beam_set.DicomPlanLabel)]\\r\\n      Alternative snippet: RtStructureSetsReferencedFromBeamSets = \\r\\n      [beam_set.BeamSetIdentifier()]\\r\\n    BeamSets - List of beamset identifiers that shall be \\r\\n      exported\\r\\n      The identifier shall be specified as PlanName:DicomPlanLabel \\r\\n      (ex. \\\"Plan 1:BS 1\\\" for plan \\\"Plan 1\\\" with beam set \\\"BS 1\\\")\\r\\n      Argument snippet: BeamSets = [\\\"%s:%s\\\"%(plan.Name, \\r\\n      beam_set.DicomPlanLabel)]\\r\\n      Alternative snippet: BeamSets = [beam_set.BeamSetIdentifier()]\\r\\n    BeamSetDoseForBeamSets - List of beamset identifiers for \\r\\n      which the beam set dose shall be exported \\r\\n      The identifier shall be specified as PlanName:DicomPlanLabel \\r\\n      (ex. \\\"Plan 1:BS 1\\\" for plan \\\"Plan 1\\\" with beam set \\\"BS 1\\\")\\r\\n      Argument snippet: BeamSetDoseForBeamSets = \\r\\n      [\\\"%s:%s\\\"%(plan.Name, beam_set.DicomPlanLabel)]\\r\\n      Alternative snippet: BeamSetDoseForBeamSets = \\r\\n      [beam_set.BeamSetIdentifier()]\\r\\n    BeamDosesForBeamSets - List of beamset identifiers for \\r\\n      which all beam doses shall be exported \\r\\n      The identifier shall be specified as PlanName:DicomPlanLabel \\r\\n      (ex. \\\"Plan 1:BS 1\\\" for plan \\\"Plan 1\\\" with beam set \\\"BS 1\\\")\\r\\n      Argument snippet: BeamDosesForBeamSets = [\\\"%s:%s\\\"%(plan.Name, \\r\\n      beam_set.DicomPlanLabel)]\\r\\n      Alternative snippet: BeamDosesForBeamSets = \\r\\n      [beam_set.BeamSetIdentifier()]\\r\\n    SpatialRegistrationForExaminations - List of examination \\r\\n      pairs for which the registration object shall be exported.\\r\\n      The pair is specified as fromExaminationName:toExaminationName\\r\\n      Argument snippet: SpatialRegistrationForExaminations = \\r\\n      [\\\"%s:%s\\\"%(fromExamination.Name, toExamination.Name)]\\r\\n    TreatmentBeamDrrImages - List of beamset identifiers for \\r\\n      which all treatment beam DRRs shall be exported \\r\\n      The identifier shall be specified as PlanName:DicomPlanLabel \\r\\n      (ex. \\\"Plan 1:BS 1\\\" for plan \\\"Plan 1\\\" with beam set \\\"BS 1\\\")\\r\\n      Argument snippet: TreatmentBeamDrrImages =  \\r\\n      [\\\"%s:%s\\\"%(plan.Name, beam_set.DicomPlanLabel)]\\r\\n      Alternative snippet: TreatmentBeamDrrImages = \\r\\n      [beam_set.BeamSetIdentifier()]\\r\\n      If you want to specify a single beam or specific DrrSetting \\r\\n      other then Default, the identifier shall be specified as \\r\\n      PlanName:DicomPlanLabel:BeamName:DrrSettingName\\r\\n      (ex. \\\"Plan 1:BS 1:B 1:DRR 1\\\" for plan \\\"Plan 1\\\", with beam set \\r\\n      \\\"BS 1\\\", and beam \\\"B 1\\\" and DrrSetting \\\"DRR 1\\\"\\r\\n      The last two argument can be omitted if wanted. \\r\\n      Not specifying beam will take all beams in the beam set\\r\\n      Not specifying DrrSetting will use the setting named \\\"Default\\\"\\r\\n      Argument snippet: TreatmentBeamDrrImages =  \\r\\n      [\\\"%s:%s:%s:%s\\\"%(plan.Name, beam_set.DicomPlanLabel, \\\"\\\", \\\"\\\")] # \\r\\n      all beams with Default DrrSetting\\r\\n      Argument snippet: TreatmentBeamDrrImages =  \\r\\n      [\\\"%s:%s:%s:%s\\\"%(plan.Name, beam_set.DicomPlanLabel, \\\"\\\", \\\"DRR \\r\\n      1\\\")] # all beams with DrrSetting named \\\"DRR 1\\\"\\r\\n      Argument snippet: TreatmentBeamDrrImages =  \\r\\n      [\\\"%s:%s:%s:%s\\\"%(plan.Name, beam_set.DicomPlanLabel, beam.Name, \\r\\n      \\\"\\\")] # only the selected beam with Default DrrSetting\\r\\n      Argument snippet: TreatmentBeamDrrImages =  \\r\\n      [\\\"%s:%s:%s:%s\\\"%(plan.Name, beam_set.DicomPlanLabel, beam.Name, \\r\\n      \\\"DRR 1\\\")] # only the selected beam with DrrSetting named \\\"DRR 1\\\"\\r\\n    SetupBeamDrrImages - List of beamset identifiers for which \\r\\n      all setup beam DRRs shall be exported \\r\\n      The identifier shall be specified as PlanName:DicomPlanLabel \\r\\n      (ex. \\\"Plan 1:BS 1\\\" for plan \\\"Plan 1\\\" with beam set \\\"BS 1\\\")\\r\\n      Argument snippet: SetupBeamDrrImages =  [\\\"%s:%s\\\"%(plan.Name, \\r\\n      beam_set.DicomPlanLabel)]\\r\\n      Alternative snippet: SetupBeamDrrImages = \\r\\n      [beam_set.BeamSetIdentifier()]\\r\\n      If you want to specify a single beam or specific DrrSetting \\r\\n      other then Default, the identifier shall be specified as \\r\\n      PlanName:DicomPlanLabel:BeamName:DrrSettingName\\r\\n      (ex. \\\"Plan 1:BS 1:B 1:DRR 1\\\" for plan \\\"Plan 1\\\", with beam set \\r\\n      \\\"BS 1\\\", and beam \\\"B 1\\\" and DrrSetting \\\"DRR 1\\\"\\r\\n      The last two argument can be omitted if wanted. \\r\\n      Not specifying beam will take all beams in the beam set\\r\\n      Not specifying DrrSetting will use the setting named \\\"Default\\\"\\r\\n      Argument snippet: SetupBeamDrrImages =  \\r\\n      [\\\"%s:%s:%s:%s\\\"%(plan.Name, beam_set.DicomPlanLabel, \\\"\\\", \\\"\\\")] # \\r\\n      all beams with Default DrrSetting\\r\\n      Argument snippet: SetupBeamDrrImages =  \\r\\n      [\\\"%s:%s:%s:%s\\\"%(plan.Name, beam_set.DicomPlanLabel, \\\"\\\", \\\"DRR \\r\\n      1\\\")] # all beams with DrrSetting named \\\"DRR 1\\\"\\r\\n      Argument snippet: SetupBeamDrrImages =  \\r\\n      [\\\"%s:%s:%s:%s\\\"%(plan.Name, beam_set.DicomPlanLabel, beam.Name, \\r\\n      \\\"\\\")] # only the selected beam with Default DrrSetting\\r\\n      Argument snippet: SetupBeamDrrImages =  \\r\\n      [\\\"%s:%s:%s:%s\\\"%(plan.Name, beam_set.DicomPlanLabel, beam.Name, \\r\\n      \\\"DRR 1\\\")] # only the selected beam with DrrSetting named \\\"DRR 1\\\"\\r\\n    DicomFilter - Dicom filter to use during export. Specified \\r\\n      by filter name.\\r\\n    IgnorePreConditionWarnings - Switch for disabeling \\r\\n      warnings. For any clinical export, warnings must be handled by \\r\\n      first exporting with this argument set to False.\\r\\n      Use a try - except pattern to catch all warnings. After the \\r\\n      warnings been handled, the export can bu run again with this \\r\\n      attribute\\r\\n      set to True.\\r\\n      Code snippet:\\r\\n      try:\\r\\n        case.ScriptableDicomExport(...)\\r\\n      except SystemError as error:\\r\\n        HandleWarnings(error)\\r\\n        case.ScriptableDicomExport(... \\r\\n      IgnorePreConditionWarnings=True)\\r\\n\"}")
