import lib.lib as lib
import json
def easyCheck(s):
    return "AddNewAdaptedBeamSet" in s
def scoreForDict(d):
    import sys
    if not isinstance(d, dict):
        return sys.maxint
    arguments_right_result = argumentsRight(d)
    if arguments_right_result != True:
        return (float(arguments_right_result) + float(prefixScore(d)))/2.0
    return sys.maxint
def argumentsRight(d):
    args = ["AdaptToRadiationSet","RemoveBeams","ClearBeamModifiers","Name","ExaminationName","MachineName","Modality","TreatmentTechnique","*Conformal","*SMLC","*VMAT","*DMLC","*StaticArc","*TomoHelical","*ProtonPencilBeamScanning","*LineScanning","*UniformScanning","*Wobbling","*SingleScattering","*DoubleScattering","*ApplicatorAndCutout","*CarbonPencilBeamScanning","PatientPosition","NumberOfFractions","CreateSetupBeams","UseLocalizationPointAsSetupIsocenter","Comment","RbeModelReference","EnableDynamicTrackingForVero"]
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
    from bases import score_Plan
    steps += 1
    score_temp = lib.score_generic(d, "AddNewAdaptedBeamSet")
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    steps += 1
    score_temp = score_Plan.get_score(d.get("value"))
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    return float(score) / float(steps)
def get_info():
    return json.loads("{\"base\": \"Plan\", \"params\": [\"AdaptToRadiationSet\", \"RemoveBeams\", \"ClearBeamModifiers\", \"Name\", \"ExaminationName\", \"MachineName\", \"Modality\", \"TreatmentTechnique\", \"*Conformal\", \"*SMLC\", \"*VMAT\", \"*DMLC\", \"*StaticArc\", \"*TomoHelical\", \"*ProtonPencilBeamScanning\", \"*LineScanning\", \"*UniformScanning\", \"*Wobbling\", \"*SingleScattering\", \"*DoubleScattering\", \"*ApplicatorAndCutout\", \"*CarbonPencilBeamScanning\", \"PatientPosition\", \"NumberOfFractions\", \"CreateSetupBeams\", \"UseLocalizationPointAsSetupIsocenter\", \"Comment\", \"RbeModelReference\", \"EnableDynamicTrackingForVero\"], \"method\": \"AddNewAdaptedBeamSet\", \"description\": \"AddNewAdaptedBeamSet(..)\\r\\n  Composite action for adding\\r\\n  Parameters:\\r\\n    AdaptToRadiationSet - Radiation set to adapt to.\\r\\n    RemoveBeams - Set to true if all beams should be removed.\\r\\n      If both RemoveBeams and ClearBeamModifiers are true,\\r\\n      beams will be removed. If both are false, nothing will be done.\\r\\n    ClearBeamModifiers - Set to true if beam contents should \\r\\n      be cleared.\\r\\n      If both RemoveBeams and ClearBeamModifiers are true,\\r\\n      beams will be removed. If both are false, nothing will be done.\\r\\n    Name - The name of the new beam set.\\r\\n    ExaminationName - The name of the examination on which the \\r\\n      beam set is defined.\\r\\n    MachineName - The name on the treatment machine. The \\r\\n      latest commissioned version og this machine will be used.\\r\\n    Modality - The treatment modality.\\r\\n      * Photons\\r\\n      * Protons\\r\\n      * Carbon\\r\\n      * Electrons\\r\\n    TreatmentTechnique - Treatment technique.\\r\\n      * Conformal                - Photons 3DCRT treatment technique.\\r\\n      * SMLC                     - Photons SMLC treatment technique.\\r\\n      * VMAT                     - Photons VMAT treatment technique\\r\\n      * DMLC                     - Photons DMLC.\\r\\n      * StaticArc                - Photons static arc.\\r\\n      * TomoHelical              - Photons tomo helical.\\r\\n      * ProtonPencilBeamScanning - Protons pencil beam scanning.\\r\\n      * LineScanning             - Protons line scanning.\\r\\n      * UniformScanning          - Protons uniform scanning.\\r\\n      * Wobbling                 - Protons wobbling scanning.\\r\\n      * SingleScattering         - Protons single scattering.\\r\\n      * DoubleScattering         - Protons double scattering.\\r\\n      * ApplicatorAndCutout      - Electrons applicator and cutout.\\r\\n      * CarbonPencilBeamScanning - Carbon pencil beam scanning.\\r\\n    PatientPosition - Specifies the position of the patient \\r\\n      relative to the treatment/image equipment space.\\r\\n      * HeadFirstProne\\r\\n      * HeadFirstSupine\\r\\n      * FeetFirstProne\\r\\n      * FeetFirstSupine\\r\\n      * HeadFirstDecubitusLeft\\r\\n      * HeadFirstDecubitusRight\\r\\n      * FeetFirstDecubitusLeft\\r\\n      * FeetFirstDecubitusRight\\r\\n    NumberOfFractions - The number of fractions in the new \\r\\n      beam set.\\r\\n    CreateSetupBeams - Whether setup beams shall be created in \\r\\n      this beam set.\\r\\n    UseLocalizationPointAsSetupIsocenter - True to use \\r\\n      localization point instead of isocenter from treatment beams \\r\\n      for the setup beams\\r\\n    Comment - The beam set comment\\r\\n    RbeModelReference - The RBE model to use for an ion \\r\\n      radiation set; or null if no RBE model is used\\r\\n    EnableDynamicTrackingForVero - Indicates if Dynamic \\r\\n      tracking for the Vero Linac is enabled or disabled\\r\\n\"}")
