@echo off
echo password | "C:\Program Files\AnyDesk\anydesk.exe" Anydesk_ID
if %errorlevel% neq 0 (
    echo Connection lost. Powering on remote device...
    "C:\Program Files\AnyDesk\anydesk.exe" 1415734603 --remote-restart
    timeout /t 1
    echo Remote device powered on. Reconnecting...
    goto loop
) else (
    echo Connected. Waiting for 10 seconds...
    timeout /t 10
    goto loop
)
