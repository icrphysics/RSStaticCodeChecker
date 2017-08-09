import lib.lib as lib
import json
def easyCheck(s):
    return "AddDosePrescriptionToPoi" in s
def scoreForDict(d):
    import sys
    if not isinstance(d, dict):
        return sys.maxint
    arguments_right_result = argumentsRight(d)
    if arguments_right_result != True:
        return (float(arguments_right_result) + float(prefixScore(d)))/2.0
    return sys.maxint
def argumentsRight(d):
    args = ["PoiName","DoseValue","RelativePrescriptionLevel","AutoScaleDose"]
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
    score_temp = lib.score_generic(d, "AddDosePrescriptionToPoi")
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
    score_temp = score_Case.get_score(d.get("value").get("value").get("value").get("value").get("value"))
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    return float(score) / float(steps)
def get_info():
    return json.loads("{\"base\": \"Case.TreatmentPlans.[].BeamSets.[]\", \"params\": [\"PoiName\", \"DoseValue\", \"RelativePrescriptionLevel\", \"AutoScaleDose\"], \"method\": \"AddDosePrescriptionToPoi\", \"description\": \"AddDosePrescriptionToPoi(..)\\r\\n  Defines a prescription to the beam set dose. If the beamset has \\r\\n  background dose, the prescription will relate to the plan dose.\\r\\n  Parameters:\\r\\n    PoiName - Name of the poi the prescription will be defined \\r\\n      on.\\r\\n    DoseValue - The prescribed dose [cGy].\\r\\n    RelativePrescriptionLevel - The relative prescription \\r\\n      level, or prescription percentage. \\r\\n      For default behaviour, set to 1.0. \\r\\n      If set to for instance 0.95 it shall be interpreted in the \\r\\n      following way (for PrescriptionType = AverageDose, DoseValue = \\r\\n      4000 cGy):\\r\\n                  \\r\\n      95% of the Average dose in the roi shall be 4000 cGy. \\r\\n                  \\r\\n      (The actual average dose in the roi will be the 4000 cGy \\r\\n      divided by 0.95)\\r\\n    AutoScaleDose - True if the planning dose should \\r\\n      automatically be kept scaled to the prescribed dose.\\r\\n\"}")
