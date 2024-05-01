@echo off
setlocal enabledelayedexpansion

rem Kiểm tra xem Python 3.10.9 đã được cài đặt
echo ---------------------------------------------------------
python --version 2>nul
if %errorlevel% neq 0 (
    echo Python 3.10.9 is not installed.
    exit /b 1
) else (
    echo Python is already installed.
)

echo ---------------------------------------------------------
rem Kiểm tra xem pip đã được cài đặt
python -m pip --version 2>nul
if %errorlevel% neq 0 (
    echo Installing pip...

    rem Tải và cài đặt get-pip.py từ trang chính thức của pip
    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    python get-pip.py

    rem Xác nhận cài đặt pip
    python -m pip --version 2>nul
    if %errorlevel% neq 0 (
        echo Error: Failed to install pip.
        exit /b 1
    )
    echo pip installed successfully.
) else (
    echo pip is already installed.
)

echo ---------------------------------------------------------
rem Cài đặt các gói từ requirements.txt
python -m pip install -r requirements.txt

echo ---------------------------------------------------------
echo Setup completed successfully!
