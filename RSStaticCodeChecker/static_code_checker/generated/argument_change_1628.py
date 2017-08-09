import lib.lib as lib
import json
def easyCheck(s):
    return "CreateQAPlan" in s
def scoreForDict(d):
    import sys
    if not isinstance(d, dict):
        return sys.maxint
    arguments_right_result = argumentsRight(d)
    if arguments_right_result != True:
        return (float(arguments_right_result) + float(prefixScore(d)))/2.0
    return sys.maxint
def argumentsRight(d):
    args = ["PhantomName","PhantomId","QAPlanName","IsoCenter","DoseGrid","GantryAngle","CollimatorAngle","CouchAngle","ComputeDoseWhenPlanIsCreated","NumberOfMonteCarloHistories"]
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
    score_temp = lib.score_generic(d, "CreateQAPlan")
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
    return json.loads("{\"base\": \"Case.TreatmentPlans.[].BeamSets.[]\", \"params\": [\"PhantomName\", \"PhantomId\", \"QAPlanName\", \"IsoCenter\", \"DoseGrid\", \"GantryAngle\", \"CollimatorAngle\", \"CouchAngle\", \"ComputeDoseWhenPlanIsCreated\", \"NumberOfMonteCarloHistories\"], \"method\": \"CreateQAPlan\", \"description\": \"CreateQAPlan(..)\\r\\n  Creates a QA plan for a beam set.\\r\\n  Parameters:\\r\\n    PhantomName - The name of the phantom used for the QA \\r\\n      plan. Requierd property.\\r\\n    PhantomId - The ID of the phantom used for the QA plan. \\r\\n      Required property.\\r\\n    QAPlanName - The name of the QA plan. Required property. \\r\\n      The name of the QA plan must be unique among the QA plans for \\r\\n      the same treatment plan beam set.\\r\\n    IsoCenter - The position of the isocenter in the phantom. \\r\\n      Expressed in the DICOM coordinate system.\\r\\n    DoseGrid - The resolution of the QA plan dose grid. The \\r\\n      dose grid is constructed to cover the outline of the phantom.\\r\\n    GantryAngle - The value of the gantry angle(s) for the \\r\\n      beams in the plan. Can be null. If a gantry angle is provided, \\r\\n      all beams in the plan will be \\r\\n      collapsed to this angle (all beams will have the same gantry \\r\\n      angle). If a gantry angle is not provided, the beams in the QA \\r\\n      plan will have\\r\\n      the same gantry angles as the beams in the treatment plan. \\r\\n      Angles are defined as in IEC standard.\\r\\n    CollimatorAngle - The value of the collimator angle(s) for \\r\\n      the beams in the plan. Can be null. If a collimator angle is \\r\\n      provided, all beams in the plan will be \\r\\n      collapsed to this angle (all beams will have the same \\r\\n      collimator angle). If a collimator angle is not provided, the \\r\\n      beams in the QA plan will have\\r\\n      the same collimator angles as the beams in the treatment plan. \\r\\n      Angles are defined as in IEC standard.\\r\\n    CouchAngle - The value of the couch angle(s) for the beams \\r\\n      in the plan. Can be null. If a couch angle is provided all \\r\\n      beams in the plan will be \\r\\n      collapsed to this angle (all beams will have the same couch \\r\\n      angle). If a couch angle is not provided, the beams in the QA \\r\\n      plan will have\\r\\n      the same couch angles as the beams in the treatment plan. \\r\\n      Angles are defined as in IEC standard.\\r\\n    ComputeDoseWhenPlanIsCreated - A switch for computing the \\r\\n      dose for the QA plan when it is created.\\r\\n    NumberOfMonteCarloHistories - Number of Monte Carlo \\r\\n      histories (for ElectronMonteCarlo)\\r\\n\"}")
