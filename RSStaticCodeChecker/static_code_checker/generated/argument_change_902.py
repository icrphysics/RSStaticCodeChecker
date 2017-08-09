import lib.lib as lib
import json
def easyCheck(s):
    return "DeliverPlanOnMultipleImageSets" in s
def scoreForDict(d):
    import sys
    if not isinstance(d, dict):
        return sys.maxint
    arguments_right_result = argumentsRight(d)
    if arguments_right_result != True:
        return (float(arguments_right_result) + float(prefixScore(d)))/2.0
    return sys.maxint
def argumentsRight(d):
    args = ["FractionNumber","SegmentWeightsPerExamination"]
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
    score_temp = lib.score_generic(d, "DeliverPlanOnMultipleImageSets")
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
    return json.loads("{\"base\": \"BeamSet.DrrSettings.[].BeamListSource\", \"params\": [\"FractionNumber\", \"SegmentWeightsPerExamination\"], \"method\": \"DeliverPlanOnMultipleImageSets\", \"description\": \"DeliverPlanOnMultipleImageSets(..)\\r\\n  Computes dose on multiple examinations, using selected beams and \\r\\n  segments for each examination.\\r\\n  (Only PBS (clinical), SMLC and VMAT (non-clinical) supported so \\r\\n  far.)\\r\\n  Parameters:\\r\\n    FractionNumber - The number of the fraction for which the \\r\\n      dose is to be computed. Default is 0.\\r\\n    SegmentWeightsPerExamination - A dictionary of what \\r\\n      segments and beams should be computed on which examinations.\\r\\n      First the examination is given, then the beam name, and \\r\\n      finally the segment number and the corresponding weight for \\r\\n      that examination.\\r\\n      Example: SegmentWeightsPerExamination = { 'CT 1' : { 'Beam 1' \\r\\n      : { '0' : 0.5, '2': 0.2 } }, 'CT 2' : { 'Beam 1' : { '0': 0.5, \\r\\n      '1': 1, '2': 0.8 } } }\\r\\n\"}")
