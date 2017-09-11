import client_lib_config
import requests
import json
from multiprocessing import Pool
import sys
import os

def find_in_folder(folder, no_of_processes = 3, traverse = True, suffixes = (".py")):
    """
    Does the static code checker for all files in a folder by using multiprocessing techniques
    @params traverse: Should also sub folders be consideres (recoursively)? (default is True)
    @params suffixes: Which files should be considered? (default is (".py")) Don't enter a list, but a tuple
    """
    files = get_check_files_in_folder(folder, traverse, suffixes)
    import time
    start_time = time.time()

    pool = Pool(processes=no_of_processes)
    results_deep = pool.map(find_in_file, files)
    results = [ent for sublist in results_deep for ent in sublist]
    
    print "done"
    end_time = time.time()
    hours, rem = divmod(end_time - start_time, 3600)
    minutes, seconds = divmod(rem, 60)
    timestr = "==> Execution time: {:0>2} h {:0>2} m {:05.2f} s".format(int(hours),int(minutes),seconds)
    print(timestr)
    return results

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

def find_in_file(f):
    print "File: {}".format(f)
    results = []
    with open(f, 'r') as myfile:
        data=myfile.read()
        temp_results = find_in_code(data)
        for r in temp_results:
            r["file"] = f
        results.extend(temp_results)
    return results

def find_in_code(code):
    r = requests.post(client_lib_config.get_server(), data={"code": code})
    if not r.text:
        return []
    return json.loads(r.text)

def start_server():
    if server_is_up():
        print "server is up"
        return
    path_to_start = os.getenv('RayStationStaticCodeCheckerServerBat')
    os.system("start cmd /K \"{}\"".format(path_to_start))
    print "start cmd /K \"{}\"".format(path_to_start)
    print "Waiting for start up of server..."
    while not server_is_up():
        continue
    print "Server has started!"
    
def server_is_up():
    import socket

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    up = False
    try:
        s.bind(("0.0.0.0", client_lib_config.get_port()))
    except socket.error as e:
        up = True
        if e.errno == 98:
            pass
        else:
            # something else raised the socket.error exception
            pass

    s.close()
    return up
    

def main():
    """
    The method for the command line tool for the static_code_checker_client heart script.

    Excerpt of the README:

    ## Use the Static Code Checker Client
    ### Check folder (requires normal python environment for multiprocessing)
    1.	`> . code_scanner.sh --folder "C:/somewhere/"`
    ### Check file
    1.	`> . code_scanner.sh --file "C:/file.py"`
    ### Check code
    1.	`> . code_scanner.sh --code "patient.attribute.DoSomething(a=2)"`
    ### Output suffix arguments
    #### Print JSON result set in console (default)
    #### Save non-formatted Output JSON in JSON file
    1.	Add `--output` argument (e.g. `> . code_scanner.sh --folder "C:/somewhere/" --output "C:/output.json"`)
    #### Save well-formatted Output JSON in JSON file
    1.	Add `--output` argument 
    2.	Add `--format` argument that is set to `True`
    (e.g. `> . code_scanner.sh --folder "C:/somewhere/" --output "C:/output.json" --format True`)
    #### Save as human-readable HTML file
    1.	Add `--ouput` argument and specify the html file as which it should be saved
    2.	Add `--html` argument and write True behind it
    (e.g. `> . code_scanner.sh --folder "C:/somewhere/" --output "C:/results.html" --html True`)

    """
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", help="The file that should be analyzed")             
    parser.add_argument("--folder", help="The folder that should be analyzed")
    parser.add_argument("--code", help="The code that should be analyzed")
    parser.add_argument("--output", help="If given the results will be serialized in this file")
    parser.add_argument("--processes", help="The max number of parallel processes that should be used when checking a folder.")
    parser.add_argument("--html", help="If output was specified, should it be printed as html?")
    parser.add_argument("--format", help="If output was specified, should it be serialized in a prettyfied way?")
    parser.add_argument("--noserver", help="Will not start the server even though it may not be running.")
    args = parser.parse_args()

    if not args.noserver:
        start_server()

    results = []
    if args.code:
        results = find_in_code(args.code)
    elif args.file:
        results = find_in_file(args.file)
    elif args.folder:
        if args.processes:
            results = find_in_folder(args.folder, args.processes)
        else:
            results = find_in_folder(args.folder)
    
    if args.output:
        with open(args.output, "w") as f:
            if args.html or args.output.lower().endswith(".html"):
                import json_to_html_output
                s = json_to_html_output.to_html(json.dumps(results, indent=4, sort_keys=True, ensure_ascii=False, encoding='utf-8'))
                f.write(s)
            elif args.format:
                f.write(json.dumps(results, indent=4, sort_keys=True, ensure_ascii=False, encoding='utf-8'))
            else:
                f.write(json.dumps(results, ensure_ascii=False, encoding='utf-8'))
        print "Saved results in file {}".format(args.output)
    else:
        print json.dumps(results, indent = 4, sort_keys=True, ensure_ascii=False, encoding='utf-8')
    
    return results

if __name__ == "__main__":
    main()