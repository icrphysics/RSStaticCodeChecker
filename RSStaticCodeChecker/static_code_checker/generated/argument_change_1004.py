import lib.lib as lib
import json
def easyCheck(s):
    return "CreateStructuresFromTemplate" in s
def scoreForDict(d):
    import sys
    if not isinstance(d, dict):
        return sys.maxint
    arguments_right_result = argumentsRight(d)
    if arguments_right_result != True:
        return (float(arguments_right_result) + float(prefixScore(d)))/2.0
    return sys.maxint
def argumentsRight(d):
    args = ["SourceTemplateName","SourceExaminationName","SourceRoiNames","SourcePoiNames","AssociateStructuresByName","TargetExamination","InitializationOption"]
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
    score_temp = lib.score_generic(d, "CreateStructuresFromTemplate")
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    steps += 1
    score_temp = lib.score_generic(d.get("value"), "RoiListSource")
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    steps += 1
    score_temp = lib.score_generic(d.get("value").get("value"), "OnDensity")
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
    score_temp = lib.score_generic(d.get("value").get("value").get("value").get("value"), "BeamDoses")
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    steps += 1
    score_temp = lib.score_generic(d.get("value").get("value").get("value").get("value").get("value"), "FractionDose")
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    steps += 1
    score_temp = lib.score_generic(d.get("value").get("value").get("value").get("value").get("value").get("value"), "BeamListSource")
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    steps += 1
    score_temp = lib.score_generic(d.get("value").get("value").get("value").get("value").get("value").get("value").get("value"), "[]")
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    steps += 1
    score_temp = lib.score_generic(d.get("value").get("value").get("value").get("value").get("value").get("value").get("value").get("value"), "DrrSettings")
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    steps += 1
    score_temp = score_BeamSet.get_score(d.get("value").get("value").get("value").get("value").get("value").get("value").get("value").get("value").get("value"))
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    return float(score) / float(steps)
def get_info():
    return json.loads("{\"base\": \"BeamSet.DrrSettings.[].BeamListSource.FractionDose.BeamDoses.[].OnDensity.RoiListSource\", \"params\": [\"SourceTemplateName\", \"SourceExaminationName\", \"SourceRoiNames\", \"SourcePoiNames\", \"AssociateStructuresByName\", \"TargetExamination\", \"InitializationOption\"], \"method\": \"CreateStructuresFromTemplate\", \"description\": \"CreateStructuresFromTemplate(..)\\r\\n  Create structures from template.\\r\\n  Parameters:\\r\\n    SourceTemplateName - The source template name.\\r\\n    SourceExaminationName - The name of the source (template) \\r\\n      examination.\\r\\n    SourceRoiNames - List of source (template) ROIs.\\r\\n    SourcePoiNames - List of source (template) POIs.\\r\\n    AssociateStructuresByName - Sets whether to associate \\r\\n      structures by name. \\r\\n      - If false, target structures with the same name as template \\r\\n      structures will be duplicated, \\r\\n        i.e., a new ROI or POI will be created and a suffix will be \\r\\n      added to the name.\\r\\n      - If true, target structures that are empty will be populated. \\r\\n      Non-empty target structures will be disregarded.\\r\\n      The default value is true.\\r\\n    TargetExamination - The target examination.\\r\\n    InitializationOption - Initialization option. Possible \\r\\n      values;\\r\\n      * EmptyGeometries\\r\\n      * AlignImageCenters\\r\\n      * RigidRegistration\\r\\n\"}")
