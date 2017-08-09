import lib.lib as lib
import json
def easyCheck(s):
    return "CreateRoi" in s
def scoreForDict(d):
    import sys
    if not isinstance(d, dict):
        return sys.maxint
    arguments_right_result = argumentsRight(d)
    if arguments_right_result != True:
        return (float(arguments_right_result) + float(prefixScore(d)))/2.0
    return sys.maxint
def argumentsRight(d):
    args = ["Name","Color","Type","TissueName","RbeCellTypeName","RoiMaterial"]
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
    score_temp = lib.score_generic(d, "CreateRoi")
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    steps += 1
    score_temp = lib.score_generic(d.get("value"), "PatientModel")
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    steps += 1
    score_temp = score_Case.get_score(d.get("value").get("value"))
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    return float(score) / float(steps)
def get_info():
    return json.loads("{\"base\": \"Case.PatientModel\", \"params\": [\"Name\", \"Color\", \"Type\", \"TissueName\", \"RbeCellTypeName\", \"RoiMaterial\"], \"method\": \"CreateRoi\", \"description\": \"CreateRoi(..)\\r\\n  Create a new ROI.\\r\\n  Parameters:\\r\\n    Name - The name of the new ROI.\\r\\n    Color - Display color of the ROI. Use a color such as \\r\\n      'Red' or an ARGB value such as '#FFFF0000'.\\r\\n    Type - ROI type. Possible values;\\r\\n      * External: External patient contour.\\r\\n      * Ptv: Planning target volume (as defined in ICRU50).\\r\\n      * Ctv: Clinical target volume (as defined in ICRU50).\\r\\n      * Gtv: Gross tumor volume (as defined in ICRU50).\\r\\n      * TreatedVolume: Treated volume (as defined in ICRU50).\\r\\n      * IrradiatedVolume: Irradiated Volume (as defined in ICRU50).\\r\\n      * Bolus: Patient bolus to be used for external beam therapy.\\r\\n      * Avoidance: Region in which dose is to be minimized.\\r\\n      * Organ: Patient organ.\\r\\n      * Marker: Patient marker or marker on a localizer.\\r\\n      * Registration: Registration ROI\\r\\n      * Isocenter: Treatment isocenter to be used for external beam \\r\\n      therapy.\\r\\n      * ContrastAgent: Volume into which a contrast agent has been \\r\\n      injected.\\r\\n      * Cavity: Patient anatomical cavity.\\r\\n      * BrachyChannel: Branchy therapy channel\\r\\n      * BrachyAccessory: Brachy therapy accessory device.\\r\\n      * BrachySourceApplicator: Brachy therapy source applicator.\\r\\n      * BrachyChannelShield: Brachy therapy channel shield.\\r\\n      * Support: External patient support device.\\r\\n      * Fixation: External patient fixation or immobilisation device.\\r\\n      * DoseRegion: ROI to be used as a dose reference.\\r\\n      * Control: ROI to be used in control of dose optimization and \\r\\n      calculation.\\r\\n      * FieldOfView: ROI to be used for representing the \\r\\n      Field-of-view in, e.g., a cone beam CT image.\\r\\n      * AcquisitionIsocenter: Acquisition isocenter, the position \\r\\n      during acquisition.\\r\\n      * InitialLaserIsocenter: Initial laser isocenter, the position \\r\\n      before acquisition.\\r\\n      * InitialMatchIsocenter: Initial match isocenter, the position \\r\\n      after acquisition.\\r\\n      * Undefined.\\r\\n    TissueName - Name of the organ tissue. Optional.\\r\\n    RbeCellTypeName - Name of the organ RBE cell type. Optional.\\r\\n    RoiMaterial - Material that overrides ROI density. Optional.\\r\\n\"}")
