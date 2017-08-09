import lib.lib as lib
import json
def easyCheck(s):
    return "ComputeDose" in s
def scoreForDict(d):
    import sys
    if not isinstance(d, dict):
        return sys.maxint
    arguments_right_result = argumentsRight(d)
    if arguments_right_result != True:
        return (float(arguments_right_result) + float(prefixScore(d)))/2.0
    return sys.maxint
def argumentsRight(d):
    args = ["ComputeBeamDoses","DoseAlgorithm","ForceRecompute"]
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
    score_temp = lib.score_generic(d, "ComputeDose")
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
    return json.loads("{\"base\": \"BeamSet\", \"params\": [\"ComputeBeamDoses\", \"DoseAlgorithm\", \"ForceRecompute\"], \"method\": \"ComputeDose\", \"description\": \"ComputeDose(..)\\r\\n  Compute dose on a beam set.\\r\\n  Parameters:\\r\\n    ComputeBeamDoses - Indicates if beam doses shall be \\r\\n      computed. Default is true.\\r\\n    DoseAlgorithm - * CCDose: Clinical dose engine for photons \\r\\n      based on a collapsed-cone dose algorithm. Used for final dose \\r\\n      computations of all photon delivery techniques.\\r\\n      * ElectronMonteCarlo: Clinical dose engine for electrons based \\r\\n      on a Monte Carlo dose algorithm. Used for final dose \\r\\n      computations of electron plans.\\r\\n      * IonMonteCarlo: Clinical dose engine for protons based on an \\r\\n      ion Monte Carlo dose algorithm. Used for final dose \\r\\n      computations of PBS plans.\\r\\n      * SpotWeightPencilBeam: Clinical dose engine for protons based \\r\\n      on a pencil beam dose algorithm. Used for optimization and \\r\\n      final dose computations of PBS plans.\\r\\n      * IonPencilBeam: Clinical dose engine for protons based on a \\r\\n      pencil beam dose algorithm. Used for final dose computations \\r\\n      of US/DS/Wobbling plans.\\r\\n      * CarbonPencilBeam: Clinical dose engine for carbon ions based \\r\\n      on a pencil beam dose algorithm. In the presence of an RBE \\r\\n      model, both physical and RBE weighted dose are computed. Used \\r\\n      for optimization and final dose computations of PBS plans.\\r\\n      * SpotWeightPencilBeamFast: Approximate dose engine for \\r\\n      protons based on a pencil beam dose algorithm. Used for fast, \\r\\n      approximate dose computations in the optimization of PBS plans.\\r\\n      * IonPencilBeamFast: Approximate dose engine for protons based \\r\\n      on a pencil beam dose algorithm. Used for fast, approximate \\r\\n      dose computations of US/DS/Wobbling plans.\\r\\n    ForceRecompute - Set to true to force recomputation of \\r\\n      dose even if a current dose with the same dose engine already \\r\\n      exists. Default is false.\\r\\n\"}")
