import json, os
def prepare(base_info_file = None, argument_info_file = None):
    """
    Creates accepting scripts in ./generated
    Data will be used from ./information

    If not set differently with the parameters base_info_file, argument_info_file:
    The bases are stored in ./information/base.json
    The parameters are stored in ./information/parameters.json

    The bases will be in ./generated/bases
    The argument changes will be in ./generated/arguments
    The removed methods will be in ./generated/methods

    @param base_info_file: The location of the base info file. Default: ./information/base.json
    @param argument_info_file: The location of the argument info file. Default: ./information/parameters.json
    """
    if base_info_file == None:
        base_info_file = os.path.join(get_current_folder(), "information", "base.json")
    generate_base_data(base_info_file)

    if argument_info_file == None:
        argument_info_file = os.path.join(get_current_folder(), "information", "parameters.json")
    generate_argument_data(argument_info_file, base_info_file)


def generate_base_data(base_info_file):
    base_data = {}
    with open(base_info_file) as data_file:    
        base_data = json.load(data_file)

    from generator import generate_base_code

    generate_folder = os.path.join(get_current_folder(), "generated", "bases")
    for k in base_data:
        generate_base_code.generate(k, base_data[k], generate_folder)
    
def generate_argument_data(argument_info_file, base_info_file):
    base_data = {}
    with open(base_info_file) as data_file:    
        base_data = json.load(data_file)
    
    argument_data = []
    with open(argument_info_file) as data_file:    
        argument_data = json.load(data_file)

    generate_folder = os.path.join(get_current_folder(), "generated")

    from generator import generate_argument_change_code as cc
    i = 0
    for k in argument_data:
        cc.generate(i, k, base_data, generate_folder)
        i += 1

def get_current_folder():
    return os.path.dirname(os.path.realpath(__file__))