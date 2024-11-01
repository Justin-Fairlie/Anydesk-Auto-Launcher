@echo off

:loop

echo password | "C:/Program Files (x86)/AnyDesk/anydesk.exe" anydesk_id
timeout /t 1


if %errorlevel% neq 0 (
    echo Connection lost. Powering on remote device...
    "C:/Program Files (x86)/AnyDesk/anydesk.exe" %anydesk_id% --remote-restart
    echo Remote device powered on. Reconnecting...
    goto loop
) else (
    echo Connected. Waiting for 10 seconds...
    goto loop
)