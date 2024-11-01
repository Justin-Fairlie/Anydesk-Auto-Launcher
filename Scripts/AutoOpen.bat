@echo off

:loop

echo  password | "C:/Program Files/AnyDesk/anydesk.exe" ID
timeout /t 1


if %errorlevel% neq 0 (
    echo Connection lost. Powering on remote device...
    "C:/Program Files/AnyDesk/anydesk.exe" %anydesk_id% --remote-restart
    timeout /t 1
    echo Remote device powered on. Reconnecting...
    goto loop
) else (
    echo Connected. Waiting for 10 seconds...
    timeout /t 1
    goto loop
)