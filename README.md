# Ray Station Code Checker

The RayStation Code Checker is a static code analyzer that is built for recognizing the wrong usage of RayStation scripting objects / scripting methods.
# How-To
## On RayStation Update
1.	Do steps for testing library
2.	Execute `rayStationUpdate.py` (with `execfile()` in ironPython console)

## Use the Static Code Checker Client
### Check folder (requires normal python environment for multiprocessing)
1.	`> rs_code_scanner --folder "C:/somewhere/"`

### Check file
1.	`> rs_code_scanner --file "C:/file.py"`

### Check code
1.	`> rs_code_scanner --code "patient.attribute.DoSomething(a=2)"`

### Output suffix arguments
#### Print JSON result set in console (default)
#### Save non-formatted Output JSON in JSON file
1.	Add `--output` argument (e.g. `> rs_code_scanner --folder "C:/somewhere/" --output "C:/output.json"`)

#### Save well-formatted Output JSON in JSON file
1.	Add `--output` argument 
2.	Add `--format` argument that is set to `True`
(e.g. `> rs_code_scanner --folder "C:/somewhere/" --output "C:/output.json" --format True`)

#### Save as human-readable HTML file
1.	Add `--ouput` argument and specify the html file as which it should be saved
2.	Add `--html` argument and write True behind it
(e.g. `> rs_code_scanner --folder "C:/somewhere/" --output "C:/results.html" --html True`)

## Deploy to installer exe
1. Install [Inno Setup](http://www.jrsoftware.org/isinfo.php) on your computer and reboot
2. Navigate to folder in cmd.exe using the "cd" command
3. Run "create_setup_exe" (with optional version parameter, e.g. "R6") and wait a few seconds / minutes. The new exe will be in the "Output" folder (one forr x64 and x32).

### Ignore code

Sometimes the code analysis generated false positives (errors that are not actually errors).
You might want to ignore these types of errors (instead of for example renaming all your variables).
As an example the variable name "patient_list" will be interpreted as a Patient object which will result in errors when accessing it like a list.

Error types can be ignored in the next line by using this:
```
#@ignore_error_type(error_type)
```
You can also concatenate error types in this command:
```
#@ignore_error_type(attribute_error, parameter_error)
```
A variable can be ignored for the whole file by using this:
```
#@ignore_variable(patient_list)
```
where "patient_list" is the variable to ignore.

A variable can also be ignored only for a specific error types:
```
#@ignore_variable(patient_list, error_types=[attribute_error])
```
Several macros can be written in one line by separating them with "|".
```
#@ignore_error_type(attribute_error)|@ignore_error_type(parameter_error)
```