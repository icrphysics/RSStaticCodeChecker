import lib.lib as lib
import json
def easyCheck(s):
    return "SetIdcasProperties" in s
def scoreForDict(d):
    import sys
    if not isinstance(d, dict):
        return sys.maxint
    arguments_right_result = argumentsRight(d)
    if arguments_right_result != True:
        return (float(arguments_right_result) + float(prefixScore(d)))/2.0
    return sys.maxint
def argumentsRight(d):
    args = ["PatientSetupId","ImagingProtocolId"]
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
    score_temp = lib.score_generic(d, "SetIdcasProperties")
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
    score_temp = lib.score_generic(d.get("value").get("value"), "BeamSets")
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    steps += 1
    score_temp = lib.score_generic(d.get("value").get("value").get("value"), "[]")
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    steps += 1
    score_temp = lib.score_generic(d.get("value").get("value").get("value").get("value"), "TreatmentPlans")
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    steps += 1
    score_temp = lib.score_generic(d.get("value").get("value").get("value").get("value").get("value"), "[]")
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    steps += 1
    score_temp = lib.score_generic(d.get("value").get("value").get("value").get("value").get("value").get("value"), "Cases")
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    steps += 1
    score_temp = score_Patient.get_score(d.get("value").get("value").get("value").get("value").get("value").get("value").get("value"))
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    return float(score) / float(steps)
def get_info():
    return json.loads("{\"base\": \"Patient.Cases.[].TreatmentPlans.[].BeamSets.[]\", \"params\": [\"PatientSetupId\", \"ImagingProtocolId\"], \"method\": \"SetIdcasProperties\", \"description\": \"SetIdcasProperties(..)\\r\\n  Sets the patient setup and imaging protocol ID:s for the current \\r\\n  beam set \\r\\n  required for integration with the IDCAS collision avoidance \\r\\n  modules by medPhoton.\\r\\n  The id:s are communicated through the following DICOM private tags: \\r\\n    - medPhoton private creator (30BB,0010) Type 1, VR LO, VM 1 \\r\\n  Private creator identifier, always \\\"medPhoton 1.0\\\".\\r\\n    - Patient Setup ID          (30BB,1000) Type 2, VR SH, VM 1 The \\r\\n  (unique) identifier to correlate with a specified patient setup.\\r\\n    - Imaging Protocol ID       (30BB,1001) Type 2, VR SH, VM 1 The \\r\\n  (unique) identifier to correlate with a specified imaging protocol.\\r\\n  Parameters:\\r\\n    PatientSetupId - The patient setup ID. Unique identifier \\r\\n      to correlate with a specific patient setup.\\r\\n      Must not exceed 16 characters and can only contain letters, \\r\\n      digits, underscores, dashes, or dots.\\r\\n      DICOM private tag Patient Setup ID (30BB,1000).\\r\\n      If only PatientSetupId is set the ImagingProtocolId will be \\r\\n      cleared.\\r\\n    ImagingProtocolId - The imaging protocol ID. Unique \\r\\n      identifier to correlate with a specific imaging protocol.\\r\\n      Must not exceed 16 characters and can only contain letters, \\r\\n      digits, underscores, dashes, or dots.\\r\\n      DICOM private tag (30BB,1001).\\r\\n\"}")
