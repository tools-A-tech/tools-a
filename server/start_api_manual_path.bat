@echo off
setlocal
cd /d "%~dp0"

rem Change this path only when automatic detection does not work.
set "PYTHON_EXE=C:\Python38\python.exe"

if not exist "%PYTHON_EXE%" (
    echo [ERROR] File not found:
    echo %PYTHON_EXE%
    echo.
    pause
    exit /b 1
)

"%PYTHON_EXE%" "%~dp0productcms_api.py"
echo.
pause
endlocal
