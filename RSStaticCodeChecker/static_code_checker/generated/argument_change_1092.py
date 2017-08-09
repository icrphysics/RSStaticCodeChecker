import lib.lib as lib
import json
def easyCheck(s):
    return "ComputePerturbedDose" in s
def scoreForDict(d):
    import sys
    if not isinstance(d, dict):
        return sys.maxint
    arguments_right_result = argumentsRight(d)
    if arguments_right_result != True:
        return (float(arguments_right_result) + float(prefixScore(d)))/2.0
    return sys.maxint
def argumentsRight(d):
    args = ["DensityPerturbation","IsocenterShift","OnlyOneDosePerImageSet","AllowGridExpansion","ExaminationNames","FractionNumbers","ComputeBeamDoses"]
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
    score_temp = lib.score_generic(d, "ComputePerturbedDose")
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    steps += 1
    score_temp = score_BeamSet.get_score(d.get("value"))
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    return float(score) / float(steps)
def get_info():
    return json.loads("{\"base\": \"BeamSet\", \"params\": [\"DensityPerturbation\", \"IsocenterShift\", \"OnlyOneDosePerImageSet\", \"AllowGridExpansion\", \"ExaminationNames\", \"FractionNumbers\", \"ComputeBeamDoses\"], \"method\": \"ComputePerturbedDose\", \"description\": \"ComputePerturbedDose(..)\\r\\n  Compute perturbed dose on a beam set.\\r\\n  Parameters:\\r\\n    DensityPerturbation - A value of the density perturbation \\r\\n      in the present fraction. Must be in the interval -0.5 to 0.5.\\r\\n      Default value is 0.0.\\r\\n    IsocenterShift - The shift of the isocenter in the present \\r\\n      fraction in the DICOM coordinate system.\\r\\n      Default value is { 'x': 0.0, 'y': 0.0, 'z': 0.0 }.\\r\\n    OnlyOneDosePerImageSet - Indicates if only one evaluation \\r\\n      dose per image set shall be allowed. \\r\\n      Previously computed evaluation doses on the selected \\r\\n      examinations will be deleted if this is set to true.\\r\\n      Default is false.\\r\\n    AllowGridExpansion - Indicates if expansion of the dose \\r\\n      grid is allowed if necessary. Default is true.\\r\\n    ExaminationNames - The names of the examinations to be \\r\\n      used. This is a required property and the number of items\\r\\n      in this list must equal the number of items in the \\r\\n      FractionNumbers property.\\r\\n    FractionNumbers - The numbers of the fractions for which \\r\\n      the dose is to be computed. This is a required property\\r\\n      and the number of items in this list must equal the number of \\r\\n      items in the ExaminationNames property. \\r\\n      This property must contain at least one item.\\r\\n    ComputeBeamDoses - Indicates if beam doses shall be \\r\\n      computed. Default is true.\\r\\n\"}")
