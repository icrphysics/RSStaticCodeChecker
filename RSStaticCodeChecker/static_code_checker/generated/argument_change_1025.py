import lib.lib as lib
import json
def easyCheck(s):
    return "CreateReportFromTemplateFile" in s
def scoreForDict(d):
    import sys
    if not isinstance(d, dict):
        return sys.maxint
    arguments_right_result = argumentsRight(d)
    if arguments_right_result != True:
        return (float(arguments_right_result) + float(prefixScore(d)))/2.0
    return sys.maxint
def argumentsRight(d):
    args = ["templateFileName","filename","ignoreWarnings"]
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
    score_temp = lib.score_generic(d, "CreateReportFromTemplateFile")
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
    return json.loads("{\"base\": \"BeamSet.DrrSettings.[].BeamListSource\", \"params\": [\"templateFileName\", \"filename\", \"ignoreWarnings\"], \"method\": \"CreateReportFromTemplateFile\", \"description\": \"CreateReportFromTemplateFile(..)\\r\\n  Create treatment plan report from template file\\r\\n  For any clinical report creation, warnings must be handled by \\r\\n  first exporting with IgnoreWarnings set to False.\\r\\n  Use a try - except pattern to catch all warnings. After the \\r\\n  warnings have been handled the export can run again with this \\r\\n  parameter set to True.\\r\\n  Code snippet:\\r\\n  try:\\r\\n    beam_set.CreateReportFromTemplateFile(... IgnoreWarnings=False)\\r\\n  except SystemError as error:\\r\\n    HandleWarnings(error)\\r\\n    beam_set.CreateReportFromTemplateFile(... IgnoreWarnings=True)\\r\\n  Parameters:\\r\\n    templateFileName - template file name (full path)\\r\\n    filename - Filename for pdf document\\r\\n    ignoreWarnings - Ignore warnings\\r\\n\"}")
