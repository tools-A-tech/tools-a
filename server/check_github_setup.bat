@echo off
setlocal
cd /d "C:\inetpub\wwwroot"
title ProductSiteCMS V1.1 GitHub Check
echo ============================================================
echo ProductSiteCMS V1.1 GitHub Check
echo ============================================================
echo.
git --version
echo.
git rev-parse --is-inside-work-tree
if errorlevel 1 goto :ERROR
echo.
echo Remote:
git remote -v
echo.
echo Branch:
git branch --show-current
echo.
echo Latest commit:
git log -1 --oneline
echo.
echo Status:
git status --short
echo.
echo [OK] GitHub connection detected.
goto :END
:ERROR
echo.
echo [ERROR] GitHub connection is incomplete.
:END
echo.
pause
endlocal
