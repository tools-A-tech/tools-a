@echo off
setlocal EnableExtensions EnableDelayedExpansion
title ProductSiteCMS V1.1 GitHub Setup

set "ROOT=C:\inetpub\wwwroot"
set "REPO=https://github.com/tools-A-tech/tools-a.git"
set "REMOTE=origin"
set "BRANCH=main"
set "BACKUP_BASE=C:\inetpub\ProductSiteCMS_backup_before_github"
set "BACKUP=%BACKUP_BASE%"

echo ============================================================
echo ProductSiteCMS V1.1 GitHub Setup
echo Repository: %REPO%
echo ============================================================
echo.

net session >nul 2>nul
if errorlevel 1 (
  echo [ERROR] Administrator permission is required.
  echo Right-click this BAT and choose Run as administrator.
  echo.
  pause
  exit /b 1
)

where git.exe >nul 2>nul
if errorlevel 1 (
  echo [ERROR] Git for Windows was not found.
  echo Install Git for Windows 2.46.2 and run this BAT again.
  echo.
  pause
  exit /b 1
)

if not exist "%ROOT%" (
  echo [ERROR] Folder not found: %ROOT%
  echo.
  pause
  exit /b 1
)

echo [1/10] Registering safe.directory...
git config --global --add safe.directory C:/inetpub/wwwroot >nul 2>nul

echo [2/10] Preparing backup...
if exist "%BACKUP%" (
  set "N=2"
  :FIND_BACKUP
  if exist "%BACKUP_BASE%_!N!" (
    set /a N+=1
    goto :FIND_BACKUP
  )
  set "BACKUP=%BACKUP_BASE%_!N!"
)
robocopy "%ROOT%" "%BACKUP%" /E /COPY:DAT /R:1 /W:1 /XD ".git" "backups" >nul
if errorlevel 8 (
  echo [ERROR] Backup failed.
  echo.
  pause
  exit /b 1
)
echo Backup: %BACKUP%

cd /d "%ROOT%"

echo [3/10] Initializing repository if needed...
if not exist ".git" git init
if errorlevel 1 goto :FAIL

echo [4/10] Configuring origin...
git remote get-url %REMOTE% >nul 2>nul
if errorlevel 1 (
  git remote add %REMOTE% "%REPO%"
) else (
  git remote set-url %REMOTE% "%REPO%"
)
if errorlevel 1 goto :FAIL

echo [5/10] Fetching GitHub history...
git fetch %REMOTE%
if errorlevel 1 (
  echo.
  echo [ERROR] GitHub fetch failed.
  echo Check internet access and repository permissions.
  goto :FAIL
)

git show-ref --verify --quiet refs/remotes/%REMOTE%/main
if errorlevel 1 (
  git show-ref --verify --quiet refs/remotes/%REMOTE%/master
  if not errorlevel 1 set "BRANCH=master"
)

echo [6/10] Switching to branch %BRANCH%...
git checkout -B %BRANCH%
if errorlevel 1 goto :FAIL

echo [7/10] Synchronizing with GitHub...
git reset --hard %REMOTE%/%BRANCH%
if errorlevel 1 goto :FAIL

echo [8/10] Restoring current CMS files...
robocopy "%BACKUP%" "%ROOT%" /E /COPY:DAT /R:1 /W:1 /XD ".git" "backups" >nul
if errorlevel 8 goto :FAIL

echo [9/10] Creating commit if changes exist...
git config user.name "ProductSiteCMS"
git config user.email "productsitecms@localhost"
git add -A
git diff --cached --quiet
if not errorlevel 1 goto :PUSH
git commit -m "Connect ProductSiteCMS V1.1"
if errorlevel 1 goto :FAIL

:PUSH
echo [10/10] Pushing to GitHub...
git push -u %REMOTE% %BRANCH%
if errorlevel 1 (
  echo.
  echo [ERROR] GitHub push failed.
  echo The local repository is already connected.
  echo Complete GitHub authentication, then run:
  echo C:\inetpub\wwwroot\server\test_github_push.bat
  echo.
  pause
  exit /b 1
)

echo.
echo ============================================================
echo [OK] ProductSiteCMS GitHub setup completed.
echo Branch: %BRANCH%
echo Backup: %BACKUP%
echo ============================================================
echo.
echo Next:
echo 1. Start C:\inetpub\wwwroot\server\start_api.bat
echo 2. Open http://192.168.11.17/admin/
echo 3. Press Ctrl+F5
echo.
pause
exit /b 0

:FAIL
echo.
echo [ERROR] Setup stopped.
echo Backup remains at:
echo %BACKUP%
echo This BAT can be run again.
echo.
pause
exit /b 1
