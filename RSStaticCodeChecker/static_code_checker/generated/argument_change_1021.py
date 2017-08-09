import lib.lib as lib
import json
def easyCheck(s):
    return "GetDoseImages" in s
def scoreForDict(d):
    import sys
    if not isinstance(d, dict):
        return sys.maxint
    arguments_right_result = argumentsRight(d)
    if arguments_right_result != True:
        return (float(arguments_right_result) + float(prefixScore(d)))/2.0
    return sys.maxint
def argumentsRight(d):
    args = ["Orientations","Points","FocusOnIsocenter","ImageSize","FocusOnRoi"]
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
    score_temp = lib.score_generic(d, "GetDoseImages")
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
    return json.loads("{\"base\": \"BeamSet.DrrSettings.[].BeamListSource\", \"params\": [\"Orientations\", \"Points\", \"FocusOnIsocenter\", \"ImageSize\", \"FocusOnRoi\"], \"method\": \"GetDoseImages\", \"description\": \"GetDoseImages(..)\\r\\n  Method for retrieving dose view images.\\r\\n  Parameters:\\r\\n    Orientations - Strings which indicate orientations, \\r\\n      transversal, coronal or sagittal (not case sensitive).\\r\\n    Points - Points in the patient coordinate system which \\r\\n      will be the centers of the views. Must be as many as the \\r\\n      Orientations.\\r\\n    FocusOnIsocenter - Indicates if the image is centered on \\r\\n      the isocenter.\\r\\n    ImageSize - The image size in nr of pixels. The \\r\\n      X-coordinate represents the width of the image [nr of pixels]. \\r\\n      The Y-coordinate represents the height of the image [nr of \\r\\n      pixels].\\r\\n    FocusOnRoi - The name of a ROI that will be in focus when \\r\\n      setting camera view.\\r\\n  Returns:\\r\\n    A dictionary mapping points to file names. Orientations are \\r\\n    in the order they were produced.\\r\\n\"}")
