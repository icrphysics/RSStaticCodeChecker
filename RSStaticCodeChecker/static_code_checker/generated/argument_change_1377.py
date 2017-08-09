import lib.lib as lib
import json
def easyCheck(s):
    return "CreateTreatmentPlanFromValidationDataSet" in s
def scoreForDict(d):
    import sys
    if not isinstance(d, dict):
        return sys.maxint
    arguments_right_result = argumentsRight(d)
    if arguments_right_result != True:
        return (float(arguments_right_result) + float(prefixScore(d)))/2.0
    return sys.maxint
def argumentsRight(d):
    args = ["ValidationDataSet","PhantomName","Plan","Name","Modality","MachineName","TreatmentTechnique","Beams","Name","MonitorUnits","SourceToSurfaceDistance","BeamQualityName","ApplicatorName","IsoCenterToSurfaceDistance","SnoutName","SnoutPosition","PrescribedSOBPRange","PrescribedSOBPWidth","SpotTuneID","SpotSpacing","NominalEnergy","FieldSize","SpotPositions","SpotWeights","Compensator","MaterialName","Thickness","BlockAperture","Type","Dimension","Position","MaxRadius","Thickness","NominalBeamEnergy","FirstScattererThickness","RidgeFilter","DoseComputationParameters","DoseEngineName","DoseGridResolution","NumberOfHistoriesPerCM2"]
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
    score_temp = lib.score_generic(d, "CreateTreatmentPlanFromValidationDataSet")
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
    return json.loads("{\"base\": \"Case\", \"params\": [\"ValidationDataSet\", \"PhantomName\", \"Plan\", \"Name\", \"Modality\", \"MachineName\", \"TreatmentTechnique\", \"Beams\", \"Name\", \"MonitorUnits\", \"SourceToSurfaceDistance\", \"BeamQualityName\", \"ApplicatorName\", \"IsoCenterToSurfaceDistance\", \"SnoutName\", \"SnoutPosition\", \"PrescribedSOBPRange\", \"PrescribedSOBPWidth\", \"SpotTuneID\", \"SpotSpacing\", \"NominalEnergy\", \"FieldSize\", \"SpotPositions\", \"SpotWeights\", \"Compensator\", \"MaterialName\", \"Thickness\", \"BlockAperture\", \"Type\", \"Dimension\", \"Position\", \"MaxRadius\", \"Thickness\", \"NominalBeamEnergy\", \"FirstScattererThickness\", \"RidgeFilter\", \"DoseComputationParameters\", \"DoseEngineName\", \"DoseGridResolution\", \"NumberOfHistoriesPerCM2\"], \"method\": \"CreateTreatmentPlanFromValidationDataSet\", \"description\": \"CreateTreatmentPlanFromValidationDataSet(..)\\r\\n  Creates an electron or ion treatment plan from a data set.\\r\\n  This action is experimental - use with care\\r\\n  Parameters:\\r\\n    ValidationDataSet - Validation data set should be in the \\r\\n      form of a dictionary with the fields listed below. Some fields \\r\\n      are specific for either electron or ion plans.\\r\\n                  \\r\\n      PhantomName           - The name of the phantom to be used in \\r\\n      the plan\\r\\n      Plan                  - This field contains information about \\r\\n      the treatment plan which will be created\\r\\n        Name                - The name of the created plan\\r\\n        Modality            - Treatment modality\\r\\n        MachineName         - The name of the machine to be used in \\r\\n      the plan\\r\\n        TreatmentTechnique  - Treatment technique: \\r\\n      \\\"ApplicatorAndCutout\\\" for electrons, \\\"DoubleScattering\\\", \\r\\n      \\\"UniformScanning\\\", \\\"Wobbling\\\", \\\"PencilBeamScanning\\\" or \\r\\n      \\\"LineScanning\\\" for ions (only PBS for carbon ions) \\r\\n        Beams               - List of beams with each beam \\r\\n      containing the information below\\r\\n          Name                        - Name of the beam\\r\\n          MonitorUnits                - Number of monitor units\\r\\n          SourceToSurfaceDistance     - Source to surface distance \\r\\n      in [cm] (only for electrons)\\r\\n          BeamQualityName             - Beam quality, e.g. \\\"E04\\\" \\r\\n      where the nominal energy is 4 MeV (only for electrons)\\r\\n          ApplicatorName              - Name of the applicator to be \\r\\n      used in the plan (only for electrons)\\r\\n          IsoCenterToSurfaceDistance  - Isocenter to phantom surface \\r\\n      distance in [cm] (only for ions)\\r\\n          SnoutName                   - The name of the snout to be \\r\\n      used (only for ions)\\r\\n          SnoutPosition               - The snout position in [cm] \\r\\n      (only for ions)\\r\\n          PrescribedSOBPRange         - The prescribed SOBP range in \\r\\n      [cm] (only for passive ions)\\r\\n          PrescribedSOBPWidth         - The prescribed SOBP \\r\\n      modulation width in [cm] (only for passive ions)\\r\\n          SpotTuneID                  - The fixed spot tune ID (only \\r\\n      for scanned ions)\\r\\n          SpotSpacing                 - The distance in [cm] between \\r\\n      spots (only for scanned ions)\\r\\n          NominalEnergy               - Nominal ion beam energy in \\r\\n      [MeV] (only for scanned ions)\\r\\n          FieldSize                   - The side in [cm] of a \\r\\n      scanned quadratic field (only for scanned ions)\\r\\n          SpotPositions               - The position of the spots \\r\\n      (only for scanned ions)\\r\\n          SpotWeights                 - The weight of each point in \\r\\n      SpotPositions (only for scanned ions)\\r\\n          Compensator                 - This field contains \\r\\n      information about range compensator (optional for passive \\r\\n      ions, may be omitted)\\r\\n            MaterialName              - Name of the range \\r\\n      compensator's material\\r\\n            Thickness                 - Thickness in [cm] of the \\r\\n      range compensator\\r\\n          BlockAperture               - The block aperture in a ions \\r\\n      plan (required for passive ions) or cutout in an electron plan \\r\\n      (optional for electrons, may be omitted)\\r\\n            Type                      - Type of block: \\\"Quadratic\\\", \\r\\n      \\\"Rectangular\\\" or \\\"SquareRoundCorners\\\"\\r\\n            Dimension                 - Dimension of block in [cm], \\r\\n      e.g. [10, 10] (for quadratic) or [10,20] (for rectangular) or \\r\\n      [15, 0] (for circular blocks) \\r\\n            Position                  - Lower corner position of \\r\\n      block in [cm]. Can only be used for blocks with Type == \\r\\n      \\\"Rectangular\\\". Format [x,y]\\r\\n            MaxRadius                 - Maximum allowed radius in \\r\\n      the isocenter plane in [cm]. Should be used for blocks with \\r\\n      Type == \\\"SquareRoundCorners\\\"\\r\\n            Thickness                 - The thickness of the block \\r\\n      in [cm]\\r\\n          NominalBeamEnergy           - The nominal beam energy \\r\\n      [MeV] (only for Sumitomo Wobbling beams)\\r\\n          FirstScattererThickness     - The first scatter thickness, \\r\\n      i.e total thickness of used lollipops [cm] (only for Sumitomo \\r\\n      Wobbling beams)\\r\\n          RidgeFilter                 - The name of the ridge filter \\r\\n      to be used (only for Sumitomo Wobbling beams)\\r\\n      DoseComputationParameters       - This field contains \\r\\n      information about the dose computation parameters\\r\\n          DoseEngineName              - The name of the dose engine \\r\\n      to be used: \\\"ElectronMonteCarlo\\\" (only for electrons), \\r\\n      \\\"IonPencilBeam\\\" (only for passive ions) or \\r\\n      \\\"SpotWeightPencilBeam\\\" (only for pbs ions) \\r\\n          DoseGridResolution          - The side of a cubic voxel in \\r\\n      [cm]\\r\\n          NumberOfHistoriesPerCM2     - The number of histories per \\r\\n      cm2 (must be specified for both electrons and ions, it is \\r\\n      however only used for the ElectronMonteCarlo dose engine)\\r\\n\"}")
