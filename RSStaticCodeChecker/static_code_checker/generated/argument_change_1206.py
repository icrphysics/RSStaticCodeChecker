import lib.lib as lib
import json
def easyCheck(s):
    return "CreateElectronBeam" in s
def scoreForDict(d):
    import sys
    if not isinstance(d, dict):
        return sys.maxint
    arguments_right_result = argumentsRight(d)
    if arguments_right_result != True:
        return (float(arguments_right_result) + float(prefixScore(d)))/2.0
    return sys.maxint
def argumentsRight(d):
    args = ["ApplicatorName","Energy","InsertName","IsAddCutoutChecked","IsocenterData","Name","Description","GantryAngle","CouchAngle","CollimatorAngle"]
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
    from bases import score_PatientDB
    steps += 1
    score_temp = lib.score_generic(d, "CreateElectronBeam")
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
    score_temp = lib.score_generic(d.get("value").get("value"), "TreatmentSetups")
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
    score_temp = lib.score_generic(d.get("value").get("value").get("value").get("value"), "TemplateTreatmentSetups")
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    steps += 1
    score_temp = score_PatientDB.get_score(d.get("value").get("value").get("value").get("value").get("value"))
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    return float(score) / float(steps)
def get_info():
    return json.loads("{\"base\": \"PatientDB.TemplateTreatmentSetups.[].TreatmentSetups.[]\", \"params\": [\"ApplicatorName\", \"Energy\", \"InsertName\", \"IsAddCutoutChecked\", \"IsocenterData\", \"Name\", \"Description\", \"GantryAngle\", \"CouchAngle\", \"CollimatorAngle\"], \"method\": \"CreateElectronBeam\", \"description\": \"CreateElectronBeam(..)\\r\\n  Creates and adds a beam of electron type.\\r\\n  Parameters:\\r\\n    ApplicatorName - Name of the electron applicator.\\r\\n    Energy - Energy [MeV] of the beam.\\r\\n    InsertName - Name of the collimating insert in the \\r\\n      applicator.\\r\\n    IsAddCutoutChecked - Gets, sets if cutout should be added\\r\\n    IsocenterData - Dictionary containing isocenter data. Use \\r\\n      help functions to create IsocenterData. \\r\\n      Example: IsocenterData = beam_set.GetIsocenterData(Name=\\\"Iso \\r\\n      1\\\") or IsocenterData = \\r\\n      beam_set.CreateDefaultIsocenterData(Position={'x':1, 'y':2, \\r\\n      'z':3} )\\r\\n    Name - Beam name, must be unique.\\r\\n    Description - Description.\\r\\n    GantryAngle - Angle unit and direction follow IEC.\\r\\n    CouchAngle - Angle unit and direction follow IEC.\\r\\n    CollimatorAngle - Angle unit and direction follow IEC.\\r\\n\"}")
