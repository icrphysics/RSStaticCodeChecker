import find_occurances, check_folder
from multiprocessing import Pool
import sys

def check_folder_async(folder, output = None, no_of_processes = 3, traverse = True, suffixes = (".py")):
    """
    Does the static code checker for all files in a folder by using multiprocessing techniques.
    This cannot be executed in an ironPython command line interface because ironPython doesn't offer a multiprocessing module.

    NOTE: Try to avoid using that function. It's a very simple implementation. Please use the static_code_checker_client and ..._server library instead.

    @param folder: The folder that should be analyzed
    @param output: The output file in which the results should be stored
    @param no_of_processes: The maximum amount of simultaniously running sub processes
    @param traverse: Whether a deep folder check should be done
    @param suffixes: Which files should be considered? (default is (".py")) Don't enter a list, but a tuple
    """
    files = check_folder.get_check_files_in_folder(folder, traverse, suffixes)
    import time
    start_time = time.time()



    pool = Pool(processes=no_of_processes)
    results_deep = pool.map(spawn, files)
    results = [ent for sublist in results_deep for ent in sublist]
    #print results

    if output:
        import json
        with open(output, "w") as f:
            f.write(json.dumps(results, sort_keys=True, indent=4))
    
    print "done"
    end_time = time.time()
    hours, rem = divmod(end_time - start_time, 3600)
    minutes, seconds = divmod(rem, 60)
    timestr = "==> Execution time: {:0>2} h {:0>2} m {:05.2f} s".format(int(hours),int(minutes),seconds)
    print(timestr)
    return results


def spawn(f):
    """
    Prints the file that will be checked next and checks the file and returns the results.
    Could easily be used for multiprocessing with a multiprocessing.Pool.
    """
    print "File: {}".format(f)
    return find_occurances.find_in_file(f)
    #shared_list.extend(result)
    #c_nprocs.value -= 1
    #finished_tasks.value += 1