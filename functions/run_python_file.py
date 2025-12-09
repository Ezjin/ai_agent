import os
import subprocess
from google import genai
from google.genai import types


schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Execute python files with optional arguments",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path to run, relative to the working directory. If not provided, will not work.",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                description="List of the arguments to run the program. It is optional",
                items=types.Schema(type=types.Type.STRING)

            )
        },
    ),
)

def run_python_file(working_directory, file_path, args=[]):
    full_path = os.path.join(working_directory, file_path)
    base = os.path.abspath(working_directory)
    target = os.path.abspath(full_path)

    if os.path.commonpath([base, target]) != base:
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    _, end = file_path.rsplit(".", 1)
    if end != "py":
        return f'Error: "{file_path}" is not a Python file.'
    

    if not os.path.isfile(full_path):
        return f'Error: File "{file_path}" not found'

    try:
        command_lst = ["uv", "run", full_path] + args
        completed_process = subprocess.run(command_lst, timeout=30, capture_output=True, text=True)
        stdout = completed_process.stdout
        stderr = completed_process.stderr
        code = completed_process.returncode
        return_string = f"STDOUT: {stdout} STDERR: {stderr}"
        if code != 0:
            return_string = return_string + f" Process exited with code {code}"

        if not stdout and not stderr:
            return "Error: No output produced"

        return return_string
    except Exception as e:
        return f"Error: executing Python file: {e}"
