import lib.lib as lib
import json
def easyCheck(s):
    return "CreatePBSIonBeam" in s
def scoreForDict(d):
    import sys
    if not isinstance(d, dict):
        return sys.maxint
    arguments_right_result = argumentsRight(d)
    if arguments_right_result != True:
        return (float(arguments_right_result) + float(prefixScore(d)))/2.0
    return sys.maxint
def argumentsRight(d):
    args = ["SnoutId","SpotTuneId","RangeShifter","MinimumAirGap","MetersetRateSetting","IsocenterData","Name","Description","GantryAngle","CouchAngle","CollimatorAngle"]
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
    score_temp = lib.score_generic(d, "CreatePBSIonBeam")
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
    score_temp = lib.score_generic(d.get("value").get("value").get("value").get("value"), "[]")
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    steps += 1
    score_temp = lib.score_generic(d.get("value").get("value").get("value").get("value").get("value"), "BeamSets")
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    steps += 1
    score_temp = score_Plan.get_score(d.get("value").get("value").get("value").get("value").get("value").get("value"))
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    return float(score) / float(steps)
def get_info():
    return json.loads("{\"base\": \"Plan.BeamSets.[].DrrSettings.[].BeamListSource\", \"params\": [\"SnoutId\", \"SpotTuneId\", \"RangeShifter\", \"MinimumAirGap\", \"MetersetRateSetting\", \"IsocenterData\", \"Name\", \"Description\", \"GantryAngle\", \"CouchAngle\", \"CollimatorAngle\"], \"method\": \"CreatePBSIonBeam\", \"description\": \"CreatePBSIonBeam(..)\\r\\n  Creates and adds a beam of PBS (or Line scanning) ion type.\\r\\n  Parameters:\\r\\n    SnoutId - Snout ID of the beam. Must be specified.\\r\\n    SpotTuneId - Name of the spot tune ID of the beam. Must be \\r\\n      specified.\\r\\n    RangeShifter - Name of the range shifter of the beam. \\r\\n      Default value is null.\\r\\n    MinimumAirGap - Minimun air gap from snout. Default value \\r\\n      is null.\\r\\n    MetersetRateSetting - MetersetRateSetting for the beam. \\r\\n      Default value is null.\\r\\n    IsocenterData - Dictionary containing isocenter data. Use \\r\\n      help functions to create IsocenterData. \\r\\n      Example: IsocenterData = beam_set.GetIsocenterData(Name=\\\"Iso \\r\\n      1\\\") or IsocenterData = \\r\\n      beam_set.CreateDefaultIsocenterData(Position={'x':1, 'y':2, \\r\\n      'z':3} )\\r\\n    Name - Beam name, must be unique.\\r\\n    Description - Description.\\r\\n    GantryAngle - Angle unit and direction follow IEC.\\r\\n    CouchAngle - Angle unit and direction follow IEC.\\r\\n    CollimatorAngle - Angle unit and direction follow IEC.\\r\\n\"}")
