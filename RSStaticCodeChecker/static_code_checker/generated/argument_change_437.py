import lib.lib as lib
import json
def easyCheck(s):
    return "ImportDicomDataFromRepository" in s
def scoreForDict(d):
    import sys
    if not isinstance(d, dict):
        return sys.maxint
    arguments_right_result = argumentsRight(d)
    if arguments_right_result != True:
        return (float(arguments_right_result) + float(prefixScore(d)))/2.0
    return sys.maxint
def argumentsRight(d):
    args = ["CaseName","Node","Port","CallingAE","CalledAE","SeriesFilter","ImportFilters"]
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
    score_temp = lib.score_generic(d, "ImportDicomDataFromRepository")
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    steps += 1
    score_temp = score_Patient.get_score(d.get("value"))
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    return float(score) / float(steps)
def get_info():
    return json.loads("{\"base\": \"Patient\", \"params\": [\"CaseName\", \"Node\", \"Port\", \"CallingAE\", \"CalledAE\", \"SeriesFilter\", \"ImportFilters\"], \"method\": \"ImportDicomDataFromRepository\", \"description\": \"ImportDicomDataFromRepository(..)\\r\\n  Imports DICOM data from a repository into this patient.\\r\\n  Example:\\r\\n    To import all series with SeriesNumber 45 to case 'CASE 1':\\r\\n    >> warnings = patient.ImportDicomDataFromRepository(CaseName = \\r\\n    \\\"CASE 1\\\", Node = \\\"node\\\", Port = 134, CallingAE = \\\"callingAE\\\", \\r\\n    CalledAE = \\\"calledAE\\\", SeriesFilter = {'SeriesNumber': '^45$'}, \\r\\n    ImportFilters = [\\\"RTPlan: Remove 0 MU beams\\\"] )\\r\\n    >> print warnings\\r\\n  Parameters:\\r\\n    CaseName - The name of the target case or null/empty if \\r\\n      new case shall be created.\\r\\n    Node - The Node.\\r\\n    Port - The port to use.\\r\\n    CallingAE - The CallingAE.\\r\\n    CalledAE - The CalledAE.\\r\\n    SeriesFilter - Filter on the series to import. Using \\r\\n      regular expressions.\\r\\n      Possible keys in SeriesFilter:\\r\\n        * Modality\\r\\n        * PatientID\\r\\n        * StudyUID\\r\\n        * StudyDescription\\r\\n        * SeriesUID\\r\\n        * SeriesDescriptiont\\r\\n        * FrameOfReferenceUid\\r\\n        * SopClassUid\\r\\n        * CreationDate\\r\\n        * SeriesDate\\r\\n        * SeriesTime\\r\\n        * SeriesNumber\\r\\n    ImportFilters - List of import filters to run (must be \\r\\n      installed in RayStation).\\r\\n  Returns:\\r\\n    Returns a string with warnings from the import.\\r\\n\"}")
