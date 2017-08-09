import os

def get_current_folder():
    return os.path.dirname(os.path.realpath(__file__))

#### Config for converter ####


#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#                                           !
raystation_version = "R6" #Version to check !
#                                           !
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!



object_types = [
    "Patient",
    "Plan",
    "BeamSet",
	"PatientDB",
    "Case",
    "Examination",
    "MachineDB",
    "ui",
    "Machine"
]

#storage_folder = os.path.join(get_current_folder(), "..", "..", "..", "test", "storage", "json_storage")
storage_folder = "/mnt/hgfs/vm_shared/json_storage"

default_file_name = "json_data_{}_{}.json".format(raystation_version, "{}")

output_file_parameters = os.path.join(get_current_folder(), "..", "information", "parameters.json")

all_attributes_output_file = os.path.join(get_current_folder(), "..", "information", "all_attributes.json")

wildcard_file = os.path.join(get_current_folder(), "..", "information", "attr_wildcards.json")



#an array that contains as many default types as possible

type_array = [0, 0.0, "", list(), True, get_current_folder, dict()]

try:
    from System.Collections.Generic import List
    type_array.append(List[int]())
except:
    pass

#### Config methods ####

def get_object_types():
    return object_types

def get_files_to_read():
    filepaths = []
    for f in object_types:
        filepaths.append(os.path.join(storage_folder, default_file_name.format(f)))
    return filepaths

def get_output_file():
    return output_file_parameters

def get_all_attributes_output_file():
    return all_attributes_output_file

def get_type_array():
    from System.Collections.Generic import List
    new_ar = type_array
    new_ar.append(List[int]())
    return new_ar

def get_wildcard_file():
    return wildcard_file