@echo off
title Auto Push GitHub

echo ==============================
echo Uploading to GitHub...
echo ==============================

cd /d "C:\Users\harshad Dhuppe\Python Programs"

git add .

git commit -m "Auto update"

git push origin main

echo.
echo ==============================
echo Push Complete!
echo ==============================

pause