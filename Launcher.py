import subprocess
import time

python_script_path = r".\Scripts\AutoClose.py"
batch_file_path = r".\Scripts\AutoOpen.bat"

# Command to run the batch file in a new terminal
batch_command = f'start cmd /k \"{batch_file_path}\"'

# Command to run the Python script in a new terminal
python_command = f'start cmd /k "python \"{python_script_path}\""'

# Execute the commands
subprocess.Popen(batch_command, shell=True)

# Wait for Anydesk to open first
time.sleep(1)
subprocess.Popen(python_command, shell=True)