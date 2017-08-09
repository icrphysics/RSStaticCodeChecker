import os

def generate(key, base_information, folder):
    """
    Generates the code for the base information
    Base information looks like this (this is json, but input of this method is a python dict):
    
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

    The output code for the exact example given, should look like this:

    # score_BeamSet.py
    def get_score(d):
        import sys
        import re
        score = sys.maxint

        if not d.get("_PyType") == "Name":
            return sys.maxint

        if re.match("^(B|b)(E|e)(A|a)(M|m)_?(S|s)(E|e)(T|t)$", d.get("id")) != None:
            score = min(score, 0)
        
        if re.match(".*(B|b)(E|e)(A|a)(M|m)_?(S|s)(E|e)(T|t).*", d.get("id")) != None:
            score = min(score, 1)
        
        if re.match(".*(B|b)(E|e)(A|a)(M|m)_?(S|s)?.*", d.get("id")) != None:
            score = min(score, 2)

        return score

    If the key ("BeamSet") contains a dot, this dot will be replaced by an underscore in the file name

    @param key: The key of the base (which will be needed for the file name)
    @param base_information: The information containing dict itself
    @param folder: The folder in which the file should be saved
    """

    file_name = "score_" + key.replace(".", "_") + ".py"
    file_path = os.path.join(folder, file_name)

    end_str = ""

    line_sep = "\n"

    #method definition and information comments
    end_str += "def get_score(d):{}".format(line_sep)
    end_str += "    \"\"\"{}".format(line_sep)
    end_str += "    checks the score for a dict representing the AST node for the base entry '{}'{}".format(key, line_sep)
    end_str += "    \"\"\"{}".format(line_sep)
    end_str += "    import sys, re{}".format(line_sep)
    end_str += "    score = sys.maxint{}".format(line_sep)
    end_str += "    if not d.get(\"_PyType\") == \"Name\":{}".format(line_sep)
    end_str += "        return sys.maxint{}".format(line_sep)

    #Add matching regex rules
    for entry in base_information:
        end_str += "    if re.match(\"{}\", d.get(\"id\")) != None:{}".format(entry.get("regex"), line_sep)
        end_str += "        score = min(score, {}){}".format(entry.get("ranking"), line_sep)
    
    end_str += "    return score"

    with open(file_path, "w") as text_file:
        text_file.write(end_str)
    
    return end_str