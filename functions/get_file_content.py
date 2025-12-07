import os
from config import MAX_CHARS

def get_file_content(working_directory, file_path):
    base = os.path.abspath(working_directory)
    file_path = os.path.join(base, file_path)
    target = os.path.abspath(file_path)

    if os.path.commonpath([base, target]) != base:
        return f"Error: Cannot read '{file_path}' as it is outside the permitted working directory"

    if not os.path.isfile(file_path):
        return f"Error: File not found or is not a regular file: '{file_path}'"

    try:
        with open(file_path, "r") as f:
            file_content_string = f.read(MAX_CHARS)

            if len(file_content_string) == MAX_CHARS:
                file_content_string = file_content_string + f"[...File '{file_path}' truncated at {MAX_CHARS} characters]"

            return file_content_string
    
    except Exception as e:
        return f"Error: Could not open the file - {e}"

