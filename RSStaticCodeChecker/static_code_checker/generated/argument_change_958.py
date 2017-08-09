import lib.lib as lib
import json
def easyCheck(s):
    return "CreateAlgebraGeometry" in s
def scoreForDict(d):
    import sys
    if not isinstance(d, dict):
        return sys.maxint
    arguments_right_result = argumentsRight(d)
    if arguments_right_result != True:
        return (float(arguments_right_result) + float(prefixScore(d)))/2.0
    return sys.maxint
def argumentsRight(d):
    args = ["Examination","Algorithm","ExpressionA","ExpressionB","ResultOperation","ResultMarginSettings"]
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
    score_temp = lib.score_generic(d, "CreateAlgebraGeometry")
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    steps += 1
    score_temp = lib.score_generic(d.get("value"), "OfRoi")
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    steps += 1
    score_temp = lib.score_generic(d.get("value").get("value"), "OutlineGeometry")
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    steps += 1
    score_temp = lib.score_generic(d.get("value").get("value").get("value"), "OnDensity")
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
    score_temp = lib.score_generic(d.get("value").get("value").get("value").get("value").get("value"), "BeamDoses")
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    steps += 1
    score_temp = lib.score_generic(d.get("value").get("value").get("value").get("value").get("value").get("value"), "FractionDose")
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    steps += 1
    score_temp = lib.score_generic(d.get("value").get("value").get("value").get("value").get("value").get("value").get("value"), "BeamListSource")
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    steps += 1
    score_temp = lib.score_generic(d.get("value").get("value").get("value").get("value").get("value").get("value").get("value").get("value"), "[]")
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    steps += 1
    score_temp = lib.score_generic(d.get("value").get("value").get("value").get("value").get("value").get("value").get("value").get("value").get("value"), "DrrSettings")
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    steps += 1
    score_temp = score_BeamSet.get_score(d.get("value").get("value").get("value").get("value").get("value").get("value").get("value").get("value").get("value").get("value"))
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    return float(score) / float(steps)
def get_info():
    return json.loads("{\"base\": \"BeamSet.DrrSettings.[].BeamListSource.FractionDose.BeamDoses.[].OnDensity.OutlineGeometry.OfRoi\", \"params\": [\"Examination\", \"Algorithm\", \"ExpressionA\", \"ExpressionB\", \"ResultOperation\", \"ResultMarginSettings\"], \"method\": \"CreateAlgebraGeometry\", \"description\": \"CreateAlgebraGeometry(..)\\r\\n  Creates an algebra geometry.\\r\\n  Parameters:\\r\\n    Examination - The examination.\\r\\n    Algorithm - Defines if the logical set operations use \\r\\n      contour or voxel based methods. \\r\\n      Margins (expand/contract) and Wall operations are always \\r\\n      performed using voxel based methods.\\r\\n                  \\r\\n      Possible values:\\r\\n      * Auto: Automatically select algorithm mode.\\r\\n      * Contours: Use contour based methods.\\r\\n      * Voxels: Use voxel based methods.\\r\\n      Default value is \\\"Auto\\\".\\r\\n    ExpressionA - Expression A. Operation must be Union or \\r\\n      Intersection.\\r\\n      Example: \\r\\n        ExpressionA = { 'Operation': \\\"Union\\\", 'SourceRoiNames': \\r\\n      [\\\"Roi A\\\", \\\"Roi B\\\"], 'MarginSettings': { 'Type': \\\"Expand\\\", \\r\\n      'Superior': 1, 'Inferior': 1, 'Anterior': 1, 'Posterior': 1, \\r\\n      'Right': 1, 'Left': 1 } }\\r\\n    ExpressionB - Expression B. Operation must be Union or \\r\\n      Intersection.\\r\\n      Example: \\r\\n        ExpressionB = { 'Operation': \\\"Intersection\\\", \\r\\n      'SourceRoiNames': [\\\"Bladder\\\", \\\"Prostate\\\"], 'MarginSettings': { \\r\\n      'Type': \\\"Contract\\\", 'Superior': 0, 'Inferior': 0, 'Anterior': \\r\\n      0, 'Posterior': 0, 'Right': 1, 'Left': 0 } }\\r\\n    ResultOperation - The final operation to apply between \\r\\n      ExpressionA and ExpressionB. If it is None, Expression B is \\r\\n      not used.\\r\\n      Values:\\r\\n        * None\\r\\n        * Union\\r\\n        * Intersection\\r\\n        * Subtraction\\r\\n    ResultMarginSettings - The margin settings to apply to the \\r\\n      result. Defines type (Expand or Contract) and distances. All \\r\\n      distances must be positive and less than 15 cm.\\r\\n      Example: MarginSettings = { 'Type': \\\"Contract\\\", 'Superior' : \\r\\n      0.0, 'Inferior': 1.0, 'Anterior': 1.0, 'Posterior': 0.1, \\r\\n      'Right': 0.0, 'Left': 2.3 }\\r\\n\"}")
