import find_occurances

def check_folder(folder, output = None, traverse = True, suffixes = (".py")):
    """
    Does the static code checker for all files in a folder (non-multiprocessing).
    This can also be executed in an ironPython command line interface.
    See multiprocessing_foldercheck for a multiprocessing implementation that can only run in the normal python command line interface.

    @param folder: The folder that should be analyzed
    @param output: The output file in which the results should be stored
    @params traverse: Should also sub folders be consideres (recoursively)? (default is True)
    @params suffixes: Which files should be considered? (default is (".py")) Don't enter a list, but a tuple
    """
    files = get_check_files_in_folder(folder, traverse, suffixes)
    import time
    start_time = time.time()
    results = []
    for i, f in enumerate(files):
        print "[{}/{}({:.1f}%)] {}".format(i, len(files), (float(i)/float(len(files)))*100.0,f)
        results.extend(find_occurances.find_in_file(f, (i==0)))
    print ""
    print ""
    print "RESULT:"
    print "   Found a total of {} potential errors in the following files:".format(len(results))
    for f in get_files_in_result_set(results):
        print "     - \"{}\":\n          {} potential error{}".format(f.get("file"), f.get("count"), "s" if f.get("count") > 1 else "")
    
    end_time = time.time()
    hours, rem = divmod(end_time - start_time, 3600)
    minutes, seconds = divmod(rem, 60)
    print("==> Execution time: {:0>2} h {:0>2} m {:05.2f} s".format(int(hours),int(minutes),seconds))
    if output:
        import json
        with open(output, "w") as f:
            f.write(json.dumps(results, sort_keys=True, indent=4))
    return results
    
def get_files_in_result_set(results):
    """
    Receives a list of results from the static code checker and returns a list of files and the amount of found errors.
    @param results: The result set that was generated by the static code checker
    @returns: a list containing dicts that have the "file" and "count" attributes
    """
    files = []
    for r in results:
        found = False
        for f in files:
            if f.get("file") == r.get("file"):
                f["count"] += 1
                found = True
        if not found:
            files.append({"file": r.get("file"), "count": 1})
    return files

def get_check_files_in_folder(folder, traverse, suffixes = (".py")):
    """
    Returns a list of all files (their full file paths) that should be checked in a directory
    """
    import os
    onlyfiles = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]
    files_to_check = []
    for f in onlyfiles:
        if f.endswith(suffixes):
            files_to_check.append(os.path.join(folder, f))
    if not traverse:
        return files_to_check
    
    dirs = [d for d in os.listdir(folder) if os.path.isdir(os.path.join(folder, d))]
    for d in dirs:
        files_to_check.extend(get_check_files_in_folder(os.path.join(folder, d), True, suffixes))

    return files_to_check


import sys, os
def main():
    import argparse, json
    parser = argparse.ArgumentParser()
    parser.add_argument("f")
    args = parser.parse_args()
    blockPrint()
    results = check_folder(args.f)
    enablePrint()
    print json.dumps(results)


# Disable
def blockPrint():
    sys.stdout = open(os.devnull, 'w')

# Restore
def enablePrint():
    sys.stdout = sys.__stdout__


if __name__ == "__main__": main()

