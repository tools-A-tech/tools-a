@echo off
setlocal
cd /d "%~dp0"
title ProductSiteCMS API Test
echo ============================================================
echo ProductSiteCMS V0.8.3 Local API Test
echo ============================================================
echo.
echo Testing API from this Win7 PC: http://127.0.0.1:8765/api/status
echo.
powershell -NoProfile -ExecutionPolicy Bypass -Command "try { (New-Object Net.WebClient).DownloadString('http://127.0.0.1:8765/api/status') } catch { Write-Host '[ERROR]' $_.Exception.Message; exit 1 }"
echo.
if errorlevel 1 (
    echo API is not running or port 8765 is blocked.
) else (
    echo API connection succeeded.
)
echo.
pause
endlocal
