from functions.get_file_content import get_file_content
from functions.get_files_info import get_files_info
from functions.run_python_file import run_python_file
from functions.write_file import write_file
from google import genai
from google.genai import types

def call_function(function_call_part, verbose=False):
    WORKING_DIRECTORY = "./calculator/"
    available_functions = {
        "get_file_content": get_file_content,
        "get_files_info": get_files_info,
        "run_python_file": run_python_file,
        "write_file": write_file,
    }

    function_name = function_call_part.name

    if verbose:
        print(f"Calling function: {function_name} ({function_call_part.args})")
    else:
        print(f" - Calling function: {function_name}")
        

    try:
        function_result = available_functions[function_name](WORKING_DIRECTORY, **function_call_part.args)
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_name,
                    response={"result": function_result}
                )
            ]
        )
    except:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_name,
                    response={"error": f"Unknown function: {function_name}"},
                )
            ],
        )

