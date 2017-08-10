import json
import os
def to_html(raw):
    data = json.loads(raw)
    s = ""
    template = ""
    package_directory = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(package_directory, "template.html"), "r") as f:
        template = f.read()
    
    s += "<h2>({})</h2>".format(len(data))
    for result in data:
        s += "<div class='result'>"
        s += "<div class='file attr'>"
        s += result["file"]
        s += "</div>"
        s += "<div class='description attr'>Description: <b>"
        s += result["description"]
        s += "</b></div>"
        if result.get("alternatives") and len(result.get("alternatives")):
            s += "<div class='alternatives attr'>Did you mean: <b>"
            for i, a in enumerate(result.get("alternatives")):
                s += "</br>.{}".format(a.replace(".[]", "[index]"))
            s += "</b></div>"
        s += "<div class='line attr'> line: <b>"
        s += str(result["lineno"])
        s += "</b>"
        if "col_offset" in result:
            s += ":" + str(result["col_offset"])
        s += "</div>"
        s += "<div class='error_code attr'>Error Code: <b>"
        s += result["error_code"]
        s += "</b></div>"
        s += "<div class='error_type attr'>"
        s += result["error_type"]
        s += "</div>"
        if "info" in result:
            s += "<div class='attr'><b>Method documentation:</b></div>"
            s += "<div class='info attr'>"
            s += result["info"]["description"].encode('ascii', 'ignore').replace("\n", "<br>")
            s += "</div>"
        try:
            with open(result["file"], 'r') as f:
                lines = f.read().splitlines()
                line = lines[result['lineno'] - 1]
                s += "<div class='attr'><b>Code line preview:</b></div>"
                s += "<div class='info attr'>".format(result["file"])
                s += line
                s += "</div>"
        except:
            pass
        s += "</div>"
    
    s += "<div class='raw'>"
    s += raw
    s += "</div>"
    return template.replace('{}', s)