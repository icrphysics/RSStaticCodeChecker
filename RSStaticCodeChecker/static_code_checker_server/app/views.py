from flask import redirect
from flask import request
import find_occurances
from flask import current_app as app
import json

@app.route('/', methods=["POST", "GET"])
def main():
    """
    This API is made up of just one root which is the base root.
    To use it the "code" parameter is needed. Either as GET or as POST.
    The "version" parameter can be added and will then be transferred to the static_code_checker python library too.
    """
    if "code" in request.values:
        code = request.values["code"]
        v = app.config["DEFAULTRSVERSION"] if "version" not in request.values else request.values["version"]
        results = {}
        results = find_occurances.find_in_code(code, version=v)
        s = json.dumps(results)
        return s, 200
    else:
        return "", 417