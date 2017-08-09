import lib.lib as lib
import json
def easyCheck(s):
    return "CreatePoi" in s
def scoreForDict(d):
    import sys
    if not isinstance(d, dict):
        return sys.maxint
    arguments_right_result = argumentsRight(d)
    if arguments_right_result != True:
        return (float(arguments_right_result) + float(prefixScore(d)))/2.0
    return sys.maxint
def argumentsRight(d):
    args = ["Examination","Point","Volume","Name","Color","Type"]
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
    from bases import score_PatientDB
    steps += 1
    score_temp = lib.score_generic(d, "CreatePoi")
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
    score_temp = lib.score_generic(d.get("value").get("value"), "[]")
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    steps += 1
    score_temp = lib.score_generic(d.get("value").get("value").get("value"), "TemplatePatientModels")
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    steps += 1
    score_temp = score_PatientDB.get_score(d.get("value").get("value").get("value").get("value"))
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    return float(score) / float(steps)
def get_info():
    return json.loads("{\"base\": \"PatientDB.TemplatePatientModels.[].PatientModel\", \"params\": [\"Examination\", \"Point\", \"Volume\", \"Name\", \"Color\", \"Type\"], \"method\": \"CreatePoi\", \"description\": \"CreatePoi(..)\\r\\n  Create a new POI.\\r\\n  Parameters:\\r\\n    Examination - The examination on which the POI will be \\r\\n      defined. If Examination is null, Point and Volume will \\r\\n      disregarded.\\r\\n    Point - POI coordinates. Disregarded if Examination is null.\\r\\n    Volume - Volume of the point [cm^3]. Disregarded if \\r\\n      Examination is null.\\r\\n      In most cases a point has a zero volume, but if the point is \\r\\n      used to represent a detector for example, the volume can be \\r\\n      set to the volume of the detector.\\r\\n    Name - The name of the new POI.\\r\\n    Color - Display color of the POI. Use a color such as \\r\\n      'Red' or an ARGB value such as '#FFFF0000'.\\r\\n    Type - ROI type. Possible values;\\r\\n      * Marker: Patient marker or marker on a localizer.\\r\\n      * Isocenter: Treatment isocenter to be used for external beam \\r\\n      therapy.\\r\\n      * Registration.\\r\\n      * Control: To be used in control of dose optimization and \\r\\n      calculation.\\r\\n      * DoseRegion: To be used as a dose reference.\\r\\n      * LocalizationPoint: Laser coordinate system origin.\\r\\n      * AcquisitionIsocenter: Acquisition isocenter, the position \\r\\n      during acquisition.\\r\\n      * InitialLaserIsocenter: Initial laser isocenter, the position \\r\\n      before acquisition.\\r\\n      * InitialMatchIsocenter: Initial match isocenter, the position \\r\\n      after acquisition.\\r\\n      * Undefined.\\r\\n\"}")
