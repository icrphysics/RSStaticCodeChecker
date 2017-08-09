import lib.lib as lib
import json
def easyCheck(s):
    return "CreateRectangularField" in s
def scoreForDict(d):
    import sys
    if not isinstance(d, dict):
        return sys.maxint
    arguments_right_result = argumentsRight(d)
    if arguments_right_result != True:
        return (float(arguments_right_result) + float(prefixScore(d)))/2.0
    return sys.maxint
def argumentsRight(d):
    args = ["Width","Height","CenterCoordinate","MoveMLC","MoveAllMLCLeaves","MoveJaw","JawMargins","DeleteWedge","PreventExtraLeafPairFromOpening"]
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
    score_temp = lib.score_generic(d, "CreateRectangularField")
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
    score_temp = lib.score_generic(d.get("value").get("value"), "Beams")
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
    score_temp = lib.score_generic(d.get("value").get("value").get("value").get("value"), "TreatmentSetups")
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
    score_temp = lib.score_generic(d.get("value").get("value").get("value").get("value").get("value").get("value"), "TemplateTreatmentSetups")
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    steps += 1
    score_temp = score_PatientDB.get_score(d.get("value").get("value").get("value").get("value").get("value").get("value").get("value"))
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    return float(score) / float(steps)
def get_info():
    return json.loads("{\"base\": \"PatientDB.TemplateTreatmentSetups.[].TreatmentSetups.[].Beams.[]\", \"params\": [\"Width\", \"Height\", \"CenterCoordinate\", \"MoveMLC\", \"MoveAllMLCLeaves\", \"MoveJaw\", \"JawMargins\", \"DeleteWedge\", \"PreventExtraLeafPairFromOpening\"], \"method\": \"CreateRectangularField\", \"description\": \"CreateRectangularField(..)\\r\\n  Creates rectangular field.\\r\\n  Parameters:\\r\\n    Width - The width of the rectangular field in cm. Default \\r\\n      value is 1.0.\\r\\n    Height - The height of the rectangular field in cm. \\r\\n      Default value is 1.0.\\r\\n    CenterCoordinate - The center point of the rectangular \\r\\n      field in the beam coordinate system. \\r\\n      Default value is { 'x': 0, 'y': 0 }.\\r\\n    MoveMLC - Indicates if the field should be collimated by \\r\\n      the MLC. Default value is true.\\r\\n    MoveAllMLCLeaves - Indicates if all leafs should be moved \\r\\n      when adjusting MLC. Default value is false.\\r\\n    MoveJaw - Indicates if the field should be collimated by \\r\\n      the jaws. Default value is true.\\r\\n    JawMargins - The MLC to jaw margin in cm. Default value is \\r\\n      { 'x': 0, 'y': 0 }.\\r\\n    DeleteWedge - Indicates if the wedge of the beam should be \\r\\n      deleted. Default value is false.\\r\\n    PreventExtraLeafPairFromOpening - If an extra leafpair \\r\\n      should be openend, it can be prevented using this property.\\r\\n\"}")
