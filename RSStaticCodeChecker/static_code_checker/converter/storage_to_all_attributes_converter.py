from sets import Set
def storage_to_all_attributes_default():
    from checker_config import config as converterconfig
    storage_to_all_attributes(converterconfig.get_files_to_read(), converterconfig.get_all_attributes_output_file())

def storage_to_all_attributes(files_to_read, all_attributes_file):
    all_attributes = Set()
    for read_file in files_to_read:
        content = ""
        with open(read_file, "r") as f:
            content = f.read()
        underscore_split = read_file.split("_")
        base = underscore_split[-1].split(".")[0]

        import json
        d = json.loads(content)
        all_attributes |= get_all_attributes_of_dict(d, base)

    all_attributes_raw = json.dumps(list(all_attributes))
    with open(all_attributes_file, "w") as f:
        f.write(all_attributes_raw)

def get_all_attributes_of_dict(d, base):
    result = Set()
    if isinstance(d, list):
        new_base = "{}.[]".format(base)
        result.add(new_base)
        for element in d:
            result |= get_all_attributes_of_dict(element, new_base)
        return result
    elif isinstance(d, dict):
        for key in d:
            new_base = "{}.{}".format(base, key)
            result.add(new_base)
            result |= get_all_attributes_of_dict(d.get(key), new_base)

    return result