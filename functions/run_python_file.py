import os
import subprocess

def run_python_file(working_directory, file_path, args=[]):
    full_path = os.path.join(working_directory, file_path)
    base = os.path.abspath(working_directory)
    target = os.path.abspath(full_path)

    if os.path.commonpath([base, target]) != base:
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    _, end = file_path.rsplit(".", 1)
    if end != "py":
        return f'Error: "{file_path}" is not a Python file.'
    

    if not os.path.isfile(file_path):
        return f'Error: File "{file_path}" not found'

    try:
        command_lst = ["uv", "run", file_path] + args
        completed_process = subprocess.run(command_lst, timeout=30, capture_output=True, text=True)
        stdout = completed_process.stdout
        stderr = completed_process.stderr
        code = completed_process.returncode
        return_string = f"STDOUT: {stdout} STDERR: {stderr}"
        if code != 0:
            return_string = return_string + f" Process exited with code {code}"

        if not stdout:
            return "Error: No output produced"

        return return_string
    except Exception as e:
        return f"Error: executing Python file: {e}"
