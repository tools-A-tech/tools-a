@echo off
setlocal EnableExtensions
cd /d "C:\inetpub\wwwroot"
title ProductSiteCMS GitHub Push Test
set "BRANCH="
for /f "delims=" %%B in ('git branch --show-current') do set "BRANCH=%%B"
if not defined BRANCH set "BRANCH=main"
echo ProductSiteCMS V1.0.1 Manual Push Test
echo Branch: %BRANCH%
git add -A
git diff --cached --quiet
if not errorlevel 1 goto :PUSH
git config user.name "ProductSiteCMS"
git config user.email "productsitecms@localhost"
git commit -m "ProductSiteCMS manual publish test"
if errorlevel 1 goto :ERROR
:PUSH
git push origin %BRANCH%
if errorlevel 1 goto :ERROR
echo.
echo [OK] GitHub push completed.
goto :END
:ERROR
echo.
echo [ERROR] GitHub push failed.
echo Complete GitHub authentication and run again.
:END
echo.
pause
endlocal
