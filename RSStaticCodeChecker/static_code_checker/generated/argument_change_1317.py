import lib.lib as lib
import json
def easyCheck(s):
    return "DetectBreastMarkers" in s
def scoreForDict(d):
    import sys
    if not isinstance(d, dict):
        return sys.maxint
    arguments_right_result = argumentsRight(d)
    if arguments_right_result != True:
        return (float(arguments_right_result) + float(prefixScore(d)))/2.0
    return sys.maxint
def argumentsRight(d):
    args = ["Examination","SUPName","INFName","MEDName","LATName","ANTName","ExternalName"]
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
    score_temp = lib.score_generic(d, "DetectBreastMarkers")
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    steps += 1
    score_temp = lib.score_generic(d.get("value"), "PatientModel")
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    steps += 1
    score_temp = score_Case.get_score(d.get("value").get("value"))
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    return float(score) / float(steps)
def get_info():
    return json.loads("{\"base\": \"Case.PatientModel\", \"params\": [\"Examination\", \"SUPName\", \"INFName\", \"MEDName\", \"LATName\", \"ANTName\", \"ExternalName\"], \"method\": \"DetectBreastMarkers\", \"description\": \"DetectBreastMarkers(..)\\r\\n  For auto breast planning only.\\r\\n  Detect the SUP, INF, MED, LAT and ANT markers, and create external \\r\\n  ROI.\\r\\n  Parameters:\\r\\n    Examination - The name of the examination.\\r\\n    SUPName - Superior POI.\\r\\n    INFName - Inferior POI.\\r\\n    MEDName - Medial POI.\\r\\n    LATName - Lateral POI.\\r\\n    ANTName - Anterior POI.\\r\\n    ExternalName - External ROI.\\r\\n\"}")
