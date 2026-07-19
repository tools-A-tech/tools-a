@echo off
setlocal EnableExtensions
title ProductSiteCMS V1.1 Finish GitHub Setup
cd /d "C:\inetpub\wwwroot"

echo ============================================================
echo ProductSiteCMS V1.1 Finish Current Setup
echo ============================================================
echo.

net session >nul 2>nul
if errorlevel 1 (
  echo [ERROR] Run as administrator.
  pause
  exit /b 1
)

git config --global --add safe.directory C:/inetpub/wwwroot >nul 2>nul
git config user.name "ProductSiteCMS"
git config user.email "productsitecms@localhost"

git remote get-url origin >nul 2>nul
if errorlevel 1 git remote add origin https://github.com/tools-A-tech/tools-a.git
git remote set-url origin https://github.com/tools-A-tech/tools-a.git

git fetch origin
if errorlevel 1 goto :ERROR

git checkout -B main
if errorlevel 1 goto :ERROR

git add -A
git diff --cached --quiet
if not errorlevel 1 goto :PUSH
git commit -m "Add ProductSiteCMS V1.1"
if errorlevel 1 goto :ERROR

:PUSH
git push -u origin main
if errorlevel 1 goto :ERROR

echo.
echo [OK] Current GitHub setup completed.
echo Restart start_api.bat and refresh the admin page.
echo.
pause
exit /b 0

:ERROR
echo.
echo [ERROR] GitHub setup could not be completed.
echo Check the message above.
echo.
pause
exit /b 1
