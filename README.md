# Ray Station Code Checker

The RayStation Code Checker is a static code analyzer that is built for recognizing the wrong usage of RayStation scripting objects / scripting methods.
# Tutorial

## What Will Be Found?

The RSStaticCodeChecker uses a database containing the object structure of RayStation objects.
To detect variable name variations it uses common variable names to determine the type of a variable just by its naming (e.g. `pat` is probably a `patient` object).

The static code analysis will detect two types of errors:

### `attribute_error`

Attribute errors occur when an attribute is accessed that is not contained in the RSStaticCodeChecker database.
As an example the following line of code would result in an error:

```python
patient.Plan
```

Since the RayStation version 6 the plans are contained within `patient.Cases[index]`. The `Patient` object doesn't have a Plan attribute anymore.

The RSStaticCodeChecker will also detect the usage of indexes like:

```python
patient["Cases"][0].NonExistantAttribute
```

In this example an attribute error for `NonExistantAttribute` would be generated as an element in the list `Patient.Cases` doesn't have any attribute with that name.

The RSStaticCodeChecker will also detect when attributes are accessed like a list altough they are a dict / object / method / ... and the other way around.

```python
patient.Cases[0].PatientModel[0]    #patient.Cases[index].PatientModel is no list
patient.Cases.Name                  #patient.Cases is a list and therefore has no direct attributes
```

### `parameter_error`

Everytime a RayStation method is used it will be checked if wrong keyword arguments were used.
If for example an imaginary method called `setPatientName()` used a parameter called `name` in RayStation v5 which was renamed to `patient_name` in v6 a developer could take hours to recognize why the method doesn't have the desired effect. The RSStaticCodeChecker will recognize the error and lead you to the right solution by showing the documentation of the method.

Unfortunately RayStation doesn't document which parameters are optional / mandatory in a proper way.
That's why the code analysis will also generate errors when you don't define all keyword arguments (no matter if mandatory or optional).
Sending rather too much errors than too few errors was a decision made because we think ignoring a line takes less time than the time consuming process of starting a RayStation terminal, finding an error and then reading all the docs to find the parameter that was missing.
The score of these types of errors will be higher (which means less important, see "Score" section for more information).
Take a look at the "Ignore code" section for further information on how to ignore these lines of code for the RSStaticCodeChecker.

### The `score` information

Each error will be generated with a score. As a rule of thumb one can say:

**Low score => PRECISE MATCH / VERY IMPORTANT**

**High score => UNPRECISE MATCH / LESS IMPORTANT**

The score contains a mixture of heuristics concerning:

  - The importance of the error 
  - The probability to cause a crash or wrong behaviour in your runtime environment (e.g. wrongly spelled parameters have a lower score than missing parameters that might be optional anyways)
  - The probability of the error to actually be a proper match (e.g. `patient.WrongAttr` has a lower score than `cpat.WrongAttr`)

## Use the Static Code Checker Client Command Line Tool
### Check folder
1.	`> rs_code_scanner --folder "C:/somewhere/"`

Add a `--processes <p>` argument to define the maximum of processes that may run at the same time.

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

### Using the VSCode extension



### Ignore code

Sometimes the code analysis generates false positives (errors that are not actually errors).
You might want to ignore these types of errors (instead of for example renaming all your variables).
As an example the variable name `patient_list` will be interpreted as a Patient object which will result in errors when accessing it like a list.

Error types can be ignored in the next line by using this:
```python
#@ignore_error_type(error_type)
```
You can also concatenate error types in this command:
```python
#@ignore_error_type(attribute_error, parameter_error)
```
A variable can be ignored for the whole file by using this:
```python
#@ignore_variable(patient_list)
```
where "patient_list" is the variable to ignore.

A variable can also be ignored only for specific error types:
```python
#@ignore_variable(patient_list, error_types=[attribute_error])
```
Several macros can be written in one line by separating them with "|".
```python
#@ignore_error_type(attribute_error)|@ignore_error_type(parameter_error)
```

# Developer Information

## On RayStation Update
If you are setting up the new version of the RSStaticCodeChecker for a new RayStation version please do the following steps:
1.	Do steps for testing library
2.	Execute `rayStationUpdate.py` (with `execfile()` in ironPython console)

### Adding new Base Variables

Base variables are all variables that can be accessed via `rslOffline.get_current()` (e.g. `Patient`, `Plan`, `Case`, ...).
If new base variables were added you might want to add variable recognition information to the RSStaticCodeChecker to make it recognize these new base variables as such.

To do so open the RSStaticCodeChecker/static_code_checker/information/base.json file and add an entry that defines regexes that would detect variables of your new base variable type. You can take a look at the already existing base variable recognition information entries. It should be quite easy to copy, paste and adapt to your new base variable. The less probable the match, the higher the `ranking` attribute variable.

## Deploy to installer exe
1. Install [Inno Setup](http://www.jrsoftware.org/isinfo.php) on your computer and reboot
2. Navigate to folder in cmd.exe using the "cd" command
3. Run "create_setup_exe" (with optional version parameter, e.g. "R6") and wait a few seconds / minutes. The new exe will be in the "Output" folder (one forr x64 and x32).