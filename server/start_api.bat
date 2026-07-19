@echo off
setlocal
cd /d "%~dp0"
title ProductSiteCMS V1.1 API
echo ============================================================
echo ProductSiteCMS V1.1 API Launcher
echo ============================================================
echo.

set "PYTHON_EXE="

if exist "C:\Python38\python.exe" set "PYTHON_EXE=C:\Python38\python.exe"
if not defined PYTHON_EXE if exist "C:\Python38-32\python.exe" set "PYTHON_EXE=C:\Python38-32\python.exe"
if not defined PYTHON_EXE if exist "C:\Program Files\Python38\python.exe" set "PYTHON_EXE=C:\Program Files\Python38\python.exe"
if not defined PYTHON_EXE if exist "C:\Program Files (x86)\Python38\python.exe" set "PYTHON_EXE=C:\Program Files (x86)\Python38\python.exe"
if not defined PYTHON_EXE if exist "%LOCALAPPDATA%\Programs\Python\Python38\python.exe" set "PYTHON_EXE=%LOCALAPPDATA%\Programs\Python\Python38\python.exe"

if not defined PYTHON_EXE (
    where python.exe >nul 2>nul
    if not errorlevel 1 set "PYTHON_EXE=python.exe"
)

if not defined PYTHON_EXE (
    echo [ERROR] Python 3.8 was not found.
    echo.
    echo Run this command in Command Prompt:
    echo     where python
    echo.
    echo Then edit start_api.bat and set PYTHON_EXE manually.
    echo.
    pause
    exit /b 1
)

echo Python:
echo %PYTHON_EXE%
echo.
"%PYTHON_EXE%" --version
if errorlevel 1 (
    echo.
    echo [ERROR] Python could not be started.
    pause
    exit /b 1
)

echo.
echo Starting API on port 8765...
echo Keep this window open while using the CMS.
echo.
"%PYTHON_EXE%" "%~dp0productcms_api.py"

echo.
echo API process ended.
pause
endlocal
