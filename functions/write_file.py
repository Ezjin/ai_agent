import os

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
