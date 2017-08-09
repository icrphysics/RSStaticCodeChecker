def generate():
    from checker_config import config as converterconfig
    import json
    type_array = converterconfig.get_type_array()
    from sets import Set
    s = Set()
    for t in type_array:
        for k in dir(t):
            s.add(k)
    
    s_list = list(s)
    json_dump = json.dumps(s_list)

    output_file = converterconfig.get_wildcard_file()
    with open(output_file, "w") as f:
        f.write(json_dump)