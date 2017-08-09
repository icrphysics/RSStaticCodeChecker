import lib.lib as lib
import json
def easyCheck(s):
    return "NormalizeToPrescription" in s
def scoreForDict(d):
    import sys
    if not isinstance(d, dict):
        return sys.maxint
    arguments_right_result = argumentsRight(d)
    if arguments_right_result != True:
        return (float(arguments_right_result) + float(prefixScore(d)))/2.0
    return sys.maxint
def argumentsRight(d):
    args = ["RoiName","DoseValue","DoseVolume","PrescriptionType","LockedBeamNames","EvaluateAfterScaling"]
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
    from bases import score_BeamSet
    steps += 1
    score_temp = lib.score_generic(d, "NormalizeToPrescription")
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    steps += 1
    score_temp = lib.score_generic(d.get("value"), "BeamListSource")
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
    score_temp = lib.score_generic(d.get("value").get("value").get("value"), "DrrSettings")
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    steps += 1
    score_temp = score_BeamSet.get_score(d.get("value").get("value").get("value").get("value"))
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    return float(score) / float(steps)
def get_info():
    return json.loads("{\"base\": \"BeamSet.DrrSettings.[].BeamListSource\", \"params\": [\"RoiName\", \"DoseValue\", \"DoseVolume\", \"PrescriptionType\", \"LockedBeamNames\", \"EvaluateAfterScaling\"], \"method\": \"NormalizeToPrescription\", \"description\": \"NormalizeToPrescription(..)\\r\\n  Scales dose and the MU of the corresponding beam set.\\r\\n  Parameters:\\r\\n    RoiName - Name of ROI or POI used for dose scaling.\\r\\n    DoseValue - Dose value to scale to in cGy. \\r\\n      Must be in the interval 10 to 100000.\\r\\n    DoseVolume - Percent volume used for scaling of \\r\\n      prescription type DoseAtVolume.\\r\\n      Absolute volume (cm^3) used for scaling of prescription type \\r\\n      DoseAtAbsoluteVolume.\\r\\n      Must be in the interval 0 to 100 for prescription type \\r\\n      DoseAtVolume.\\r\\n      Must be in the interval 0 to volume of ROI for prescription \\r\\n      type DoseAtAbsoluteVolume.\\r\\n    PrescriptionType - Prescription type for scaling. Possible \\r\\n      values:\\r\\n      * AverageDose:          The average dose of the selected ROI \\r\\n      is scaled.\\r\\n                              Cannot be used for POIs. DoseVolume is \\r\\n      disregarded.\\r\\n      * DoseAtVolume:         The dose at the given percent volume \\r\\n      of the select ROI is scaled.\\r\\n                              Cannot be used for POIs.\\r\\n      * DoseAtAbsoluteVolume: The dose at the given absolute volume \\r\\n      (cm^3) of the selected ROI is scaled.\\r\\n                              Cannot be used for POIs.\\r\\n      * DoseAtPoint:          The given point dose is scaled.\\r\\n                              Can only be used for POIs.\\r\\n      * NearMinimumDose:      The dose at 98 % volume of the \\r\\n      selected ROI is scaled.\\r\\n                              Cannot be used for POIs. DoseVolume is \\r\\n      set to 98.\\r\\n      * NearMaximumDose:      The dose at 2 % volume of the selected \\r\\n      ROI is scaled.\\r\\n                              Cannot be used for POIs. DoseVolume is \\r\\n      set to 2.\\r\\n      * MedianDose:           The dose at 50 % volume of the \\r\\n      selected ROI is scaled.\\r\\n                              Cannot be used for POIs. DoseVolume is \\r\\n      set to 50.\\r\\n    LockedBeamNames - List of names of the beams that should \\r\\n      not be scaled.\\r\\n      Default value is null.\\r\\n    EvaluateAfterScaling - Indicates if the optimization \\r\\n      function values should be evaluated after scaling.\\r\\n      Default is false.\\r\\n\"}")
