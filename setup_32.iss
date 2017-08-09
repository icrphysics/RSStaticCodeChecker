; ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
;
;	The following environment variables that will be set
;		- RayStationStaticCodeCheckerPythonLibrary: path to app/static_code_checker
;		- RayStationStaticCodeCheckerClientMain:	path to app/static_code_checker_client/client_lib/main.py
;		- RayStationStaticCodeCheckerClientExe:		path to app/static_code_checker_client/code_scanner.exe
;		- RayStationStaticCodeCheckerServer:		path to app/static_code_checker_server
;		- RayStationStaticCodeCheckerServerExe:		path to app/static_code_checker_server/start.exe
;		- RayStationStaticCodeCheckerPython:		path to python inside of the winpython folder
;
;	Furthermore the static_code_checker_client will be appended to the PATH so that you can call
;		rs_code_scanner ...
;	from anywhere.
;
;	The start.exe and the code_scanner.exe were generated with http://www.f2ko.de/de/ob2e.php
;		with the respective .bat files
;
;	Destination dir for the visual studio code extensions were described here:
;		https://code.visualstudio.com/Docs/editor/extension-gallery#_common-questions	
;
; ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


                                                                                        
[Setup]                                                   
AppName=RSStaticCodeChecker                                
AppVersion=1.5                                                                                                 
DefaultDirName={pf}\RSStaticCodeChecker                                                                                                 

[Components]
Name: "main"; Description: "RSStaticCodeChecker";
Name: "extension"; Description: "VSCode extension for the  RSStaticCodeChecker"

[Files]
Source: "RSStaticCodeChecker\static_code_checker\*"; DestDir: "{app}\static_code_checker"; Components: main; Flags: ignoreversion recursesubdirs
Source: "RSStaticCodeChecker\static_code_checker_client\*"; DestDir: "{app}\static_code_checker_client"; Components: main; Flags: ignoreversion recursesubdirs
Source: "RSStaticCodeChecker\static_code_checker_server\*"; DestDir: "{app}\static_code_checker_server"; Components: main; Flags: ignoreversion recursesubdirs
Source: "RSStaticCodeChecker\WinPython-32bit\*"; DestDir: "{app}\WinPython-32bit"; Components: main; Flags: ignoreversion recursesubdirs
Source: "RSStaticCodeChecker_VSCODE_EXT\rsstaticcodechecker-vscode-ext\rsstaticcodechecker-vscode-ext-0.0.1.vsix"; DestDir: "{app}\RSStaticCodeChecker_VSCODE_EXT\rsstaticcodechecker-vscode-ext"; Components: extension; Flags: ignoreversion recursesubdirs

[Registry]
Root: HKCU; Subkey: "Environment"; ValueType:string; ValueName: "RayStationStaticCodeCheckerPythonLibrary"; \
    ValueData: "{app}\static_code_checker"; Flags: preservestringtype; Components: main
Root: HKCU; Subkey: "Environment"; ValueType:string; ValueName: "RayStationStaticCodeCheckerClientMain"; \
    ValueData: "{app}\static_code_checker_client\client_lib\main.py"; Flags: preservestringtype; Components: main
Root: HKCU; Subkey: "Environment"; ValueType:string; ValueName: "RayStationStaticCodeCheckerClientExe"; \
    ValueData: "{app}\static_code_checker_client\rs_code_scanner.exe"; Flags: preservestringtype; Components: main
    Root: HKCU; Subkey: "Environment"; ValueType:string; ValueName: "RayStationStaticCodeCheckerClientBat"; \
    ValueData: "{app}\static_code_checker_client\rs_code_scanner.bat"; Flags: preservestringtype; Components: main
Root: HKCU; Subkey: "Environment"; ValueType:string; ValueName: "RayStationStaticCodeCheckerServer"; \
    ValueData: "{app}\static_code_checker_server"; Flags: preservestringtype; Components: main
Root: HKCU; Subkey: "Environment"; ValueType:string; ValueName: "RayStationStaticCodeCheckerServerExe"; \
    ValueData: "{app}\static_code_checker_server\start.exe"; Flags: preservestringtype; Components: main
    Root: HKCU; Subkey: "Environment"; ValueType:string; ValueName: "RayStationStaticCodeCheckerServerBat"; \
    ValueData: "{app}\static_code_checker_server\start.bat"; Flags: preservestringtype; Components: main
Root: HKCU; Subkey: "Environment"; ValueType:string; ValueName: "RayStationStaticCodeCheckerPython"; \
    ValueData: "{app}\WinPython-32bit\python-2.7.13.amd32\python.exe"; Flags: preservestringtype; Components: main
Root: HKCU; Subkey: "Environment"; ValueType:string; ValueName: "RSSTATICCODECHECKERVSCODEEXT"; \
    ValueData: "{app}\RSStaticCodeChecker_VSCODE_EXT\rsstaticcodechecker-vscode-ext\rsstaticcodechecker-vscode-ext-0.0.1.vsix"; Flags: preservestringtype; Components: main
Root: HKLM; Subkey: "SYSTEM\CurrentControlSet\Control\Session Manager\Environment"; \
    ValueType: expandsz; ValueName: "Path"; ValueData: "{olddata};{app}\static_code_checker_client\"; Components: main
	
[Setup]
; Tell Windows Explorer to reload the environment
ChangesEnvironment = yes

[Run]
Filename: "{cmd}"; Parameters: "/s /c code --install-extension ""{app}\RSStaticCodeChecker_VSCODE_EXT\rsstaticcodechecker-vscode-ext\rsstaticcodechecker-vscode-ext-0.0.1.vsix"""; Components: extension

[UninstallRun]
Filename: "{cmd}"; Parameters: "/s /c code --uninstall-extension icr.rsstaticcodechecker-vscode-ext"