import lib.lib as lib
import json
def easyCheck(s):
    return "SetDensityDistributionFromImportedMetaImage" in s
def scoreForDict(d):
    import sys
    if not isinstance(d, dict):
        return sys.maxint
    arguments_right_result = argumentsRight(d)
    if arguments_right_result != True:
        return (float(arguments_right_result) + float(prefixScore(d)))/2.0
    return sys.maxint
def argumentsRight(d):
    args = ["ImageMETAHdrFileName","OverwriteExisting"]
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
    score_temp = lib.score_generic(d, "SetDensityDistributionFromImportedMetaImage")
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
    score_temp = lib.score_generic(d.get("value").get("value"), "TreatmentPlans")
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
    score_temp = lib.score_generic(d.get("value").get("value").get("value").get("value"), "Cases")
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    steps += 1
    score_temp = score_Patient.get_score(d.get("value").get("value").get("value").get("value").get("value"))
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    return float(score) / float(steps)
def get_info():
    return json.loads("{\"base\": \"Patient.Cases.[].TreatmentPlans.[]\", \"params\": [\"ImageMETAHdrFileName\", \"OverwriteExisting\"], \"method\": \"SetDensityDistributionFromImportedMetaImage\", \"description\": \"SetDensityDistributionFromImportedMetaImage(..)\\r\\n  Action for set a density distribution from information stored as \\r\\n  a meta image (http://www.itk.org/Wiki/ITK/MetaIO/Documentation) \\r\\n  Tags: \\r\\n   - Offset\\r\\n   - DimSize\\r\\n   - ElementSize \\r\\n  Should correspond to Corner in mm, NrOfVoxels, and VoxelSize in \\r\\n  mm, respectively, of the dose grid for which the density \\r\\n  distribution is defined.\\r\\n  Data is assumed to be stored in dicom coordinate system.\\r\\n  ElementType should be MET_DOUBLE\\r\\n  Parameters:\\r\\n    ImageMETAHdrFileName - \\r\\n    OverwriteExisting - \\r\\n\"}")
