@echo off

if "%1"=="" goto blank
goto witharg

:blank

iscc >nul 2>&1 && (
    iscc /Qp /F"setup_RSStaticCodeChecker_64bit" "%~dp0setup_64.iss" 
    iscc /Qp /F"setup_RSStaticCodeChecker_32bit" "%~dp0setup_32.iss" 
) || (
    "C:\Program Files (x86)\Inno Setup 5\iscc" /Qp /F"setup_RSStaticCodeChecker_64" "%~dp0setup_64.iss"
    "C:\Program Files (x86)\Inno Setup 5\iscc" /Qp /F"setup_RSStaticCodeChecker_32" "%~dp0setup_32.iss"
)

goto done

:witharg

iscc >nul 2>&1 && (
    iscc /Qp /F"setup_RSStaticCodeChecker_64_%1" "%~dp0setup_64.iss"
    iscc /Qp /F"setup_RSStaticCodeChecker_32_%1" "%~dp0setup_32.iss" 
) || (
    "C:\Program Files (x86)\Inno Setup 5\iscc" /Qp /F"setup_RSStaticCodeChecker_64_%1" "%~dp0setup_64.iss"
    "C:\Program Files (x86)\Inno Setup 5\iscc" /Qp /F"setup_RSStaticCodeChecker_32_%1" "%~dp0setup_32.iss"
)

:done