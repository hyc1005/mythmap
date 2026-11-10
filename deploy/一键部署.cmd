@echo off
chcp 65001 >nul
setlocal
cd /d "%~dp0"
set "PORT=%~1"
if not defined PORT set "PORT=8080"
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0Deploy.ps1" -Mode serve -Port %PORT% -Foreground -Open
if errorlevel 1 pause
