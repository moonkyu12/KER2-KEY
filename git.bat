@echo off
cd /d "%~dp0"
git add .
git commit -m "asd"
git push -u origin main
set /p dummy="a"