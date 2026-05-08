@echo off
title Auto Push GitHub

cd /d "C:\Users\harshad Dhuppe\Python Programs"

timeout /t 2 >nul

git add .

git diff --cached --quiet

if %errorlevel%==0 (
    echo No changes to push.
    pause
    exit
)

git commit -m "Auto update"

git push origin main

echo.
echo Push Complete!

pause