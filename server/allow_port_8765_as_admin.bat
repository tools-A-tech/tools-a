@echo off
net session >nul 2>nul
if errorlevel 1 (
    echo [ERROR] Run this file as Administrator.
    pause
    exit /b 1
)

netsh advfirewall firewall delete rule name="ProductSiteCMS API 8765" >nul 2>nul
netsh advfirewall firewall add rule name="ProductSiteCMS API 8765" dir=in action=allow protocol=TCP localport=8765 profile=private

echo.
echo Firewall rule added for TCP port 8765.
echo Restart start_api.bat and test from Win11.
echo.
pause
