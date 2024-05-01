@echo off
setlocal enabledelayedexpansion

echo ---------------------------------------------------------
echo                     CFM tool Set up
echo ---------------------------------------------------------
echo 1. Install Python
echo 2. Uninstall Python
echo ---------------------------------------------------------
set /p choice=Enter your choice (1 or 2): 

if "%choice%"=="1" (
    echo Installing Python...
    call install.bat
) else if "%choice%"=="2" (
    echo Uninstalling Python...
    call uninstall.bat
) else (
    echo Invalid choice. Please enter 1 or 2.
)

echo ---------------------------------------------------------
echo Script completed.

rem Wait for a key press to exit
echo Press any key to exit...
pause > nul
