import os, json

def generate(argument_index, argument_change_info, base_info, folder):
    """
    Uses argument_change_info that looks like this:

    {
        "base": "BeamSet.NestedAttribute",
        "method": "DoSomething",
        "new": ["necessaryParam"]
    }

    And base_info like that:
    {
    "BeamSet": [
        {
        "regex": "^(B|b)(E|e)(A|a)(M|m)_?(S|s)(E|e)(T|t)$",
        "ranking": 0
        },
        {
        "regex": ".*(B|b)(E|e)(A|a)(M|m)_?(S|s)(E|e)(T|t).*",
        "ranking": 1
        },
        {
        "regex": ".*(B|b)(E|e)(A|a)(M|m)_?(S|s)?.*",
        "ranking": 2
        }
    ],
    ...
    }

    to generate code that checks if the given dict is the given function call.

    @param argument_index: the parameter index in the storage (will be used for the file name)
    @param argument_change_info: The information that was stored in the storage
    @param base_info: The base info that is needed for the check
    @param folder: The folder in which the output file should be written
    """

    # First of all, all bases that can be found will be stored
    base = argument_change_info.get("base")
    parts = base.split('.')

    custom_bases = {}

    # choose the base information that we are interested in
    for i, part in enumerate(parts):
        whole_base = ""
        for j, part2 in enumerate(parts):
            if j == i:
                break
            whole_base += "{}.".format(part2)
        whole_base += part
        if base_info.get(whole_base) != None:
            custom_bases[whole_base] = {}
            custom_bases[whole_base]["remaining"] = parts[i+1:] + [argument_change_info.get("method")]
    
    # custom_bases now only contain those base entries that are needed and can be used

    # basic function
    end_str = ""
    end_str += "import lib.lib as lib\n"
    end_str += "import json\n"
    end_str += "def easyCheck(s):\n"
    end_str += "    return \"{}\" in s\n".format(argument_change_info.get("method"))
    end_str += "def scoreForDict(d):\n"
    end_str += "    import sys\n"
    end_str += "    if not isinstance(d, dict):\n"
    end_str += "        return sys.maxint\n"
    end_str += "    arguments_right_result = argumentsRight(d)\n"
    end_str += "    if arguments_right_result != True:\n"
    end_str += "        return (float(arguments_right_result) + float(prefixScore(d)))/2.0\n"
    end_str += "    return sys.maxint\n"


    #argument checking
    #We're checking from right to left (params first, then the last attribute, then the one before, ...)
    args = argument_change_info.get("params")
    args_string = ""
    for i,arg in enumerate(args):
        args_string += (("" if i==0 else ",") + "\"{}\"").format(arg)

    end_str += "def argumentsRight(d):\n"
    end_str += "    args = [{}]\n".format(args_string)
    end_str += "    too_many = []\n"
    end_str += "    for keyword in d.get(\"keywords\", []):\n"
    end_str += "        if keyword.get(\"arg\") in args:\n"
    end_str += "            args.remove(keyword.get(\"arg\"))\n"
    end_str += "        else:\n"
    end_str += "            too_many.append(keyword.get(\"arg\"))\n"
    end_str += "    if not too_many and not args:\n"
    end_str += "        return True\n"
    end_str += "    return (0 if too_many else 3)\n"




    # prefix score (function for checking everything prior to the arguments)
    end_str += "def prefixScore(d):\n"
    end_str += "    import sys\n"
    end_str += "    score = sys.maxint\n"
    end_str += "    steps = 0\n"
    end_str += "    if not d.get(\"_PyType\") == \"Call\":\n"
    end_str += "        return sys.maxint\n"
    end_str += "    _d = d.get(\"func\")\n"

    # now call the matching function for each found base match
    i = 0
    for k in custom_bases:
        end_str += "    score = dictMatchScore_{}(_d)\n".format(i)
        end_str += "    if score != sys.maxint:\n"
        end_str += "        return score\n"
        i += 1

    end_str += "    return sys.maxint\n"



    # now create the dictMatchScore_i function where i is the index in the base match variable
    # theoretically the order shouldn't matter as the calls can be performed in any order too
    i = 0
    for k in custom_bases:
        cb = custom_bases.get(k)
        base_module_name = "score_" + k.replace(".", "_")
        end_str += "def dictMatchScore_{}(d):\n".format(i)
        end_str += "    import sys\n"
        end_str += "    score = 0\n"
        end_str += "    steps = 0\n"
        end_str += "    from bases import {}\n".format(base_module_name) #convention

        highest = 0
        for idx, remaining in enumerate(cb.get("remaining")[::-1]):
            end_str += "    steps += 1\n"
            end_str += "    score_temp = lib.score_generic(d"
            for j in range(idx):
                end_str += ".get(\"value\")"
            end_str += ", \"{}\")\n".format(remaining)
            end_str += "    if score_temp == sys.maxint:\n"
            end_str += "        return sys.maxint\n"
            end_str += "    else:\n"
            end_str += "        score += score_temp\n"
            highest = idx
        
        end_str += "    steps += 1\n"
        end_str += "    score_temp = {}.get_score(d".format(base_module_name)
        for j in range(highest+1):
            end_str += ".get(\"value\")"
        end_str +=")\n"
        end_str += "    if score_temp == sys.maxint:\n"
        end_str += "        return sys.maxint\n"
        end_str += "    else:\n"
        end_str += "        score += score_temp\n"
        end_str += "    return float(score) / float(steps)\n"

        i += 1

    end_str += "def get_info():\n"
    end_str += "    return json.loads({})\n".format(json.dumps(json.dumps(argument_change_info)))

    file_name = "argument_change_{}.py".format(argument_index)
    file_path = os.path.join(folder, file_name)

    with open(file_path, "w") as text_file:
        text_file.write(end_str)
    
    return end_str