import lib.lib as lib
import json
def easyCheck(s):
    return "ImportMetaImageToCurrentPatient" in s
def scoreForDict(d):
    import sys
    if not isinstance(d, dict):
        return sys.maxint
    arguments_right_result = argumentsRight(d)
    if arguments_right_result != True:
        return (float(arguments_right_result) + float(prefixScore(d)))/2.0
    return sys.maxint
def argumentsRight(d):
    args = ["FrameOfReference","ExaminationName","MetaFileName","Modality","FlipZAxis"]
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
    score_temp = lib.score_generic(d, "ImportMetaImageToCurrentPatient")
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
    score_temp = lib.score_generic(d.get("value").get("value"), "Cases")
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    steps += 1
    score_temp = score_Patient.get_score(d.get("value").get("value").get("value"))
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    return float(score) / float(steps)
def get_info():
    return json.loads("{\"base\": \"Patient.Cases.[]\", \"params\": [\"FrameOfReference\", \"ExaminationName\", \"MetaFileName\", \"Modality\", \"FlipZAxis\"], \"method\": \"ImportMetaImageToCurrentPatient\", \"description\": \"ImportMetaImageToCurrentPatient(..)\\r\\n  Reads data from a meta image file \\r\\n  (http://www.itk.org/Wiki/ITK/MetaIO/Documentation) \\r\\n  and creates a new examination with a corresponding image stack for \\r\\n  the current patient.\\r\\n              \\r\\n  This method is for experimental use - use with care.\\r\\n  Support for\\r\\n  ObjectType              = Image\\r\\n  NDims                   = 3\\r\\n  BinaryData              = True\\r\\n  BinaryDataByteOrderMSB  = False\\r\\n  CompressedData          = False\\r\\n  CenterOfRotation        = 0 0 0\\r\\n  AnatomicalOrientation   = RAI\\r\\n  ElementNumberOfChannels = 1\\r\\n  ElementType             = MET_SHORT or MET_USHORT\\r\\n              \\r\\n  Patient position will be set to HFS\\r\\n              \\r\\n  Note that meta image file uses mm as unit. Hence \\r\\n  Offset/Position/Origin and ElementSize/ElementSpacing should be \\r\\n  given in mm.\\r\\n  Parameters:\\r\\n    FrameOfReference - Frame-of-reference. If empty, a new UID \\r\\n      will be generated.\\r\\n    ExaminationName - Examination name\\r\\n    MetaFileName - File name\\r\\n    Modality - \\r\\n    FlipZAxis - Apply a flip of the z-axis\\r\\n\"}")
