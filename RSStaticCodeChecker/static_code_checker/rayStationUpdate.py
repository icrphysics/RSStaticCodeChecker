import os
import glob
import prepare_for_checks

def query_yes_no(question, default="yes"):
    """Ask a yes/no question via raw_input() and return their answer.

    "question" is a string that is presented to the user.
    "default" is the presumed answer if the user just hits <Enter>.
        It must be "yes" (the default), "no" or None (meaning
        an answer is required of the user).

    The "answer" return value is True for "yes" or False for "no".
    """
    valid = {"yes": True, "y": True, "ye": True,
             "no": False, "n": False}
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        sys.stdout.write(question + prompt)
        choice = raw_input().lower()
        if default is not None and choice == '':
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' "
                             "(or 'y' or 'n').\n")

def get_current_folder():
    return os.path.dirname(os.path.realpath(__file__))

def main():
    """
    Execute this file in an ironPython console after the update of the rayStation.
    This will require the rmh.test to be fully set up for the new version.
    The following steps will take place. They are marked in the code with the respective numbers.
        1)  The JSON storage of the already setup testing library will be used to extract data that is important for the code analysis
            The data will be saved in JSON files in the "information" folder.
            Among this data are all suffix wildcards, attribute combinations and method specifications that were parsed with out of the description.
            The base.json might have to be adapted if a new base was added. Otherwise the code analysis will not find the variables.

        2)  For making the analysis very fast at runtime some python scripts will be generated and saved in the "generated" file.
            The argument_change_... scripts will offer a method that returns the matching score for the given JSON Ast tree for method parameter accuracy.
                -> information comes from "parameters.json"
            The bases/score_... scripts check if a given AST begins with the respective base. (This way e.g. "patient_obj" will be recognizes as a "Patient" base)
                -> information comes from "base.json"
            If there have been any scripts before, they will be deleted by this script so that when updating the RayStation and there are fewer argument changes the old ones will notbe executed anymore.
    """
    from checker_config import config
    
    use_config = query_yes_no("\"{}\" will be used. Is that right?".format(config.storage_folder))
    if not use_config:
        print "Please adapt the checker_config/config.py storage_folder variable accordingly"
        return
    
    convert = query_yes_no("Should the information files be overwritten now with data extracted from the storage folder?")
    if convert:
        import conv
        conv.convert_default()  #1
        print "Successfully overwritten information files with new data!"
    else:
        print "Skipping information file writing"
    
    delete_old_scripts = query_yes_no("Should all old generated checking scripts be deleted and newly generated?")
    if delete_old_scripts:
        i = 0
        while os.path.isfile(os.path.join(get_current_folder(), "generated", "argument_change_{}.py".format(i))):
            os.remove(os.path.join(get_current_folder(), "generated", "argument_change_{}.py".format(i)))
            print "Removed {}".format(os.path.join(get_current_folder(), "generated", "argument_change_{}.py".format(i)))
            i += 1
        for file_in_base_dir in glob.glob(os.path.join(os.path.join(get_current_folder(), "generated", "bases"))):
            if "__init__" in file_in_base_dir:
                continue
            print "Deleting {}".format(file_in_base_dir)
            os.remove(file_in_base_dir)
        prepare_for_checks.prepare()
        print "deleted old scripts and generated the new ones"
    print "Setup finished! You can now start the server!"


if __name__ == "__main__":
    """
    The command line implementation for this script
    """
    main()