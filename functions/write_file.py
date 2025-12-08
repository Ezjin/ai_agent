import os
from google import genai
from google.genai import types

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Write strings to file",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path to write on it, relative to the working directory. If not provided, will not work.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content to write on file"
            )
        },
    ),
)


def write_file(working_directory, file_path, content):
    file_path = os.path.join(working_directory, file_path)
    base = os.path.abspath(working_directory)
    target = os.path.abspath(file_path)

    if os.path.commonpath([base, target]) != base:
        return f"Error: Cannot write to {file_path} as it is outside the permitted working directory"

    try:
        with open(file_path, "w") as f:
            f.write(content)
            return f"Successfully wrote to '{file_path}' ({len(content)} characters written)"

    except Exception as e:
        return f"Error: Cannot write on {file_path} - {e}"
