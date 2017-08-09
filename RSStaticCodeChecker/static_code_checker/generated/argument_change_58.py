import lib.lib as lib
import json
def easyCheck(s):
    return "CreateMarkerPois" in s
def scoreForDict(d):
    import sys
    if not isinstance(d, dict):
        return sys.maxint
    arguments_right_result = argumentsRight(d)
    if arguments_right_result != True:
        return (float(arguments_right_result) + float(prefixScore(d)))/2.0
    return sys.maxint
def argumentsRight(d):
    args = ["Names","Colors"]
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
    score_temp = lib.score_generic(d, "CreateMarkerPois")
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
    score_temp = lib.score_generic(d.get("value").get("value"), "StructureSets")
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    steps += 1
    score_temp = lib.score_generic(d.get("value").get("value").get("value"), "PatientModel")
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
    score_temp = lib.score_generic(d.get("value").get("value").get("value").get("value").get("value"), "Cases")
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    steps += 1
    score_temp = score_Patient.get_score(d.get("value").get("value").get("value").get("value").get("value").get("value"))
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    return float(score) / float(steps)
def get_info():
    return json.loads("{\"base\": \"Patient.Cases.[].PatientModel.StructureSets.[]\", \"params\": [\"Names\", \"Colors\"], \"method\": \"CreateMarkerPois\", \"description\": \"CreateMarkerPois(..)\\r\\n  Identifies breast fiducials in a CT data set and creates the \\r\\n  corresponding marker POIs.\\r\\n  Parameters:\\r\\n    Names - The names of the marker POIs. Keys are: \\r\\n      \\\"Superior\\\", \\\"Inferior\\\", \\\"Lateral\\\" and \\\"Medial\\\". Values \\r\\n      defaults to: \\\"Superior\\\":\\\"MED\\\", \\\"Inferior\\\":\\\"INF\\\", \\r\\n      \\\"Medial\\\":\\\"MED\\\" and \\\"Lateral\\\":\\\"LAT\\\".\\r\\n    Colors - The display colors of the marker POIs. Use named \\r\\n      colors such as 'Red' or an ARGB value such as '#FFFF0000'. \\r\\n      Keys are: \\\"Superior\\\", \\\"Inferior\\\", \\\"Lateral\\\" and \\\"Medial\\\". \\r\\n      Values defaults to: \\\"Superior\\\":\\\"Purple\\\", \\\"Inferior\\\":\\\"Red\\\", \\r\\n      \\\"Medial\\\":\\\"Yellow\\\" and \\\"Lateral\\\":\\\"Blue\\\".\\r\\n\"}")
