import lib.lib as lib
import json
def easyCheck(s):
    return "ComputeDeliveryDoseWithDeformation" in s
def scoreForDict(d):
    import sys
    if not isinstance(d, dict):
        return sys.maxint
    arguments_right_result = argumentsRight(d)
    if arguments_right_result != True:
        return (float(arguments_right_result) + float(prefixScore(d)))/2.0
    return sys.maxint
def argumentsRight(d):
    args = ["FractionNumbers","ExaminationNames","StructureRegistrationNames"]
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
    score_temp = lib.score_generic(d, "ComputeDeliveryDoseWithDeformation")
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    steps += 1
    score_temp = lib.score_generic(d.get("value"), "TreatmentCourseSource")
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
    score_temp = lib.score_generic(d.get("value").get("value").get("value"), "PlanOptimizations")
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
    score_temp = lib.score_generic(d.get("value").get("value").get("value").get("value").get("value"), "TreatmentPlans")
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    steps += 1
    score_temp = lib.score_generic(d.get("value").get("value").get("value").get("value").get("value").get("value"), "[]")
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    steps += 1
    score_temp = lib.score_generic(d.get("value").get("value").get("value").get("value").get("value").get("value").get("value"), "Cases")
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    steps += 1
    score_temp = score_Patient.get_score(d.get("value").get("value").get("value").get("value").get("value").get("value").get("value").get("value"))
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    return float(score) / float(steps)
def get_info():
    return json.loads("{\"base\": \"Patient.Cases.[].TreatmentPlans.[].PlanOptimizations.[].TreatmentCourseSource\", \"params\": [\"FractionNumbers\", \"ExaminationNames\", \"StructureRegistrationNames\"], \"method\": \"ComputeDeliveryDoseWithDeformation\", \"description\": \"ComputeDeliveryDoseWithDeformation(..)\\r\\n  Action used to compute delivery dose and do optional deformation \\r\\n  of that dose\\r\\n  Parameters:\\r\\n    FractionNumbers - The numbers of the fractions for which \\r\\n      the dose is to be computed. This is a required property\\r\\n      and the number of items in this list must equal the number of \\r\\n      items in the ExaminationNames and\\r\\n      StructureRegistrationNames properties. This property must \\r\\n      contain at least one item.\\r\\n    ExaminationNames - The names of the examinations to be \\r\\n      used. This is a required property and the number of items\\r\\n      in this list must equal the number of items in the \\r\\n      FractionNumbers and StructureRegistrationNames\\r\\n      properties.\\r\\n    StructureRegistrationNames - The names of the provided \\r\\n      structure registrations. If an item in the list is empty, the \\r\\n      dose will\\r\\n      not be deformed. The number of items in this list must equal \\r\\n      the number of items in the\\r\\n      FractionNumbers and ExaminationNames properties.\\r\\n\"}")
