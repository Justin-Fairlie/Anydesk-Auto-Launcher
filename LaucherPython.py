import subprocess
import os

python_script_path = r"C:\Users\JustinFairlie\OneDrive - Watercare Mining\Desktop\Anydesk\Scripts\AutoClose.py"
batch_file_path = r"C:\Users\JustinFairlie\OneDrive - Watercare Mining\Desktop\Anydesk\Scripts\AutoOpen.bat"

# Command to run the Python script in a new terminal
python_command = f'start cmd /k "python \"{python_script_path}\""'

# Command to run the batch file in a new terminal
batch_command = f'start cmd /k \"{batch_file_path}\"'

# Execute the commands
subprocess.Popen(python_command, shell=True)
subprocess.Popen(batch_command, shell=True)
