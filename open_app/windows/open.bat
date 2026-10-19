@echo off
cd /d "%~dp0.."
python "%~dp0..\main.py"
if errorlevel 1 pause
