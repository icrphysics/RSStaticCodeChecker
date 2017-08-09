from converter import generate_default_attribute_wildcards, storage_to_all_attributes_converter, storage_to_argument_change_converter

def convert_default():
    #Generating wildcards
    generate_default_attribute_wildcards.generate()

    #generate attribute files for configured version
    storage_to_all_attributes_converter.storage_to_all_attributes_default()

    #generate parameter files for configured version
    storage_to_argument_change_converter.storage_to_argument_default()