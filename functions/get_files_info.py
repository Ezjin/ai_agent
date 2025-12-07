import os

def get_files_info(working_directory, directory="."):
    full_path = os.path.join(working_directory, directory)

    base = os.path.abspath(working_directory)
    target = os.path.abspath(full_path)
    
    if os.path.commonpath([base, target]) != base:
        return f'Error: Cannot list "{working_directory}" as it is outside the permitted working directory.' 

    if not os.path.isdir(full_path):
        return f'Error: "{directory}" is not a directory.'

    try:
        content_list = []
        for name in os.listdir(full_path):
            path = os.path.join(full_path, name)
            file_size = os.path.getsize(path)
            is_dir = os.path.isdir(path)
            content_list.append(f"- {name}: file_zire={file_size} bytes, is_dir={is_dir}")

        content_string = "\n".join(content_list)
        return content_string
    except Exception as e:
        return f"Error: Cannot create the string of contents. {e} "
