# Ray Station Code Checker

The RayStation Code Checker is a static code analyzer that is built for recognizing the wrong usage of RayStation scripting objects / scripting methods.
# How-To
## On RayStation Update
### Static Code Scanner Library
1.	Do steps for testing library
2.	Execute `rayStationUpdate.py` (with `execfile()` in ironPython console)
### Static Code Scanner Server
1.	Run `setup.bat`
2.	Copy `app/local_settings_example.py` to `app/local_settings.py`
3.	Adapt `local_settings.py` if needed
### Setup Static Code Checker Client
1.	Adapt `client_lib/client_lib_config.py`
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

## Deploy to installer exe
1. Install [Inno Setup](http://www.jrsoftware.org/isinfo.php) on your computer and reboot
2. Navigate to folder in cmd.exe using the "cd" command
3. Run "create_setup_exe" (with optional version parameter, e.g. "R6") and wait a few seconds / minutes. The new exe will be in the "Output" folder (one forr x64 and x32).