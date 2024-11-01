def get_details():
    # Prompt the user for ID, password, and path
    anyDeskID = input("Enter the host's AnyDesk ID: ")
    password = input("Enter your password: ")
    path = input("Enter the AnyDesk install folder path: ")

    # Write the details to a text file
    with open("Scripts/AutoOpen.bat", "w") as file:
        file.write("@echo off\n")
        file.write(f'echo {password} | "{path}\\anydesk.exe" {anyDeskID}\n')
        file.write("if %errorlevel% neq 0 (\n")
        file.write("    echo Connection lost. Powering on remote device...\n")
        file.write(f'    "{path}\\anydesk.exe" {anyDeskID} --remote-restart\n')
        file.write("    timeout /t 1\n")
        file.write("    echo Remote device powered on. Reconnecting...\n")
        file.write("    goto loop\n")
        file.write(") else (\n")
        file.write("    echo Connected. Waiting for 10 seconds...\n")
        file.write("    timeout /t 10\n")
        file.write("    goto loop\n")
        file.write(")\n")
        
    print("Details have been written to Scripts/AutoOpen.bat")

# Call the function
get_details()