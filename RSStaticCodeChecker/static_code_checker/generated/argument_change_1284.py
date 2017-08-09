import lib.lib as lib
import json
def easyCheck(s):
    return "SetAlgebraExpression" in s
def scoreForDict(d):
    import sys
    if not isinstance(d, dict):
        return sys.maxint
    arguments_right_result = argumentsRight(d)
    if arguments_right_result != True:
        return (float(arguments_right_result) + float(prefixScore(d)))/2.0
    return sys.maxint
def argumentsRight(d):
    args = ["ExpressionA","ExpressionB","ResultOperation","ResultMarginSettings"]
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
    score_temp = lib.score_generic(d, "SetAlgebraExpression")
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
    score_temp = lib.score_generic(d.get("value").get("value"), "OutlineRoiGeometry")
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
    score_temp = lib.score_generic(d.get("value").get("value").get("value").get("value"), "StructureSets")
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    steps += 1
    score_temp = lib.score_generic(d.get("value").get("value").get("value").get("value").get("value"), "PatientModel")
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    steps += 1
    score_temp = score_Case.get_score(d.get("value").get("value").get("value").get("value").get("value").get("value"))
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    return float(score) / float(steps)
def get_info():
    return json.loads("{\"base\": \"Case.PatientModel.StructureSets.[].OutlineRoiGeometry.OfRoi\", \"params\": [\"ExpressionA\", \"ExpressionB\", \"ResultOperation\", \"ResultMarginSettings\"], \"method\": \"SetAlgebraExpression\", \"description\": \"SetAlgebraExpression(..)\\r\\n  Sets a derived ROI algebra expression. The expression is defined \\r\\n  with two expressions, ExpressionA and ExpressionB, and the \\r\\n  combination of these. Should be followed by UpdateDerivedGeometry \\r\\n  in order to create the geometry for a specific examination.\\r\\n  Parameters:\\r\\n    ExpressionA - Expression A. Operation must be Union or \\r\\n      Intersection.\\r\\n      Example: \\r\\n        ExpressionA = { 'Operation': \\\"Union\\\", 'SourceRoiNames': \\r\\n      [\\\"Roi A\\\", \\\"Roi B\\\"], 'MarginSettings': { 'Type': \\\"Expand\\\", \\r\\n      'Superior': 1, 'Inferior': 1, 'Anterior': 1, 'Posterior': 1, \\r\\n      'Right': 1, 'Left': 1 } }\\r\\n    ExpressionB - Expression B. Operation must be Union or \\r\\n      Intersection.\\r\\n      Example: \\r\\n        ExpressionB = { 'Operation': \\\"Intersection\\\", \\r\\n      'SourceRoiNames': [\\\"Bladder\\\", \\\"Prostate\\\"], 'MarginSettings': { \\r\\n      'Type': \\\"Contract\\\", 'Superior': 0, 'Inferior': 0, 'Anterior': \\r\\n      0, 'Posterior': 0, 'Right': 1, 'Left': 0 } }\\r\\n    ResultOperation - The final operation to apply between \\r\\n      ExpressionA and ExpressionB. If it is None, Expression B is \\r\\n      not used.\\r\\n      Values:\\r\\n        * None\\r\\n        * Union\\r\\n        * Intersection\\r\\n        * Subtraction\\r\\n    ResultMarginSettings - The margin settings to apply to the \\r\\n      result. Defines type (Expand or Contract) and distances. All \\r\\n      distances must be positive and less than 15 cm.\\r\\n      Example: MarginSettings = { 'Type': \\\"Contract\\\", 'Superior' : \\r\\n      0.0, 'Inferior': 1.0, 'Anterior': 1.0, 'Posterior': 0.1, \\r\\n      'Right': 0.0, 'Left': 2.3 }\\r\\n\"}")
