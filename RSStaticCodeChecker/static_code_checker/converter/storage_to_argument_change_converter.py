import json

def storage_to_argument_default():
    from checker_config import config as converterconfig
    storage_to_argument(converterconfig.get_files_to_read(), converterconfig.get_output_file())

def storage_to_argument(files_to_read, parameter_file, filter_out_0_params=True):
    """
    Reads the dummy object json files (files_to_read) and extracts all the methods and their parameters to
    convert it to a parameters.json file
    @param files_to_read: Contains a list of all files that should be read and converted
    @param parameter_file: The parameter file path in which it should be saved
    @param filter_out_0_params: Should entries where len(get("params")) == 0 be filtered out (performance later on) | default = True
    """
    parameters = []
    for f in files_to_read:
        data_raw = "{}"
        with open(f, "r") as ff:
            data_raw = ff.read()
        data = json.loads(data_raw)
        #find out the base (object type)
        underscore_split = f.split("_")
        base = underscore_split[-1].split(".")[0]
        parameters.extend(get_method_dicts_of_children(data, base))
    if filter_out_0_params:
        parameters = [x for x in parameters if not (len(x.get("params")) == 0)]
    raw = json.dumps(parameters)
    with open(parameter_file, "w") as ff:
        ff.write(raw)

def get_method_dicts_of_children(di, base="Patient"):
    """
    Get's all method dicts from the children of the given dict.
    @param di: the given dict 
    """
    descr = []
    if di is None or not isinstance(di, dict):
        return descr
    for key in di:
        new_base = "{}.{}".format(base, key)
        if not isinstance(di.get(key), dict) and not isinstance(di.get(key), list):
            continue
        if isinstance(di.get(key), list):
            new_base = "{}.[]".format(new_base)
            partial_descr = []
            for el in di.get(key):
                # we could just use the first element. But what if the second element is of a different type and contains another method?
                # We will go through all elements of the list which could lead to duplicate entries. But we will filter that out at the end.
                partial_descr.extend(get_method_dicts_of_children(el, new_base)) # this could lead to duplicate entries of bases
            
            #Here we filter out the duplicates
            descr.extend(filter_out_duplicates(partial_descr))

        elif di.get(key).get("type") == "function":
            params = di.get(key).get("params")
            entry = {
                "base": base,
                "method": key,
                "params": params,
                "description": di.get(key).get("description")
            }
            descr.append(entry)
        else:
            descr.extend(get_method_dicts_of_children(di.get(key), new_base))
    return descr
	
def filter_out_duplicates(li):
    result = []
    for i, el in enumerate(li):
        found = False
        if i < len(li) - 1:
            for j, el2 in enumerate(li[i+1:]):
                if el.get("base") == el2.get("base") and el.get("method") == el2.get("method"):
                    found = True
        if not found:
            result.append(el)
    return result