@echo off
setlocal enabledelayedexpansion

rem Detect Python installation directory
set "pythonInstallPath=C:\Program Files\Python310"

rem Uninstall libraries from requirements.txt
if exist "%pythonInstallPath%" (
    echo Uninstalling libraries...
    python -m pip uninstall -r requirements.txt -y
    echo Libraries successfully uninstalled.
    echo Python installation directory deleted.
) else (
    echo Python is not installed.
)

echo ---------------------------------------------------------
echo Uninstallation completed.