import shutil


def copy_file(command: str) -> None:
    command_list = command.split()
    if len(command_list) == 3:
        function, file_in_name, file_out_name = command_list
        if (function == "cp"
                and file_in_name.endswith(".txt")
                and file_out_name.endswith(".txt")
                and file_in_name != file_out_name):
            try:
                shutil.copy(file_in_name, file_out_name)
            except FileNotFoundError:
                print(f"File '{file_in_name}' not found.")
            except PermissionError:
                print(f"Permission denied to copy '{file_in_name}' to '{file_out_name}'.")
            except Exception as e:
                print(f"An error occurred while copying the file: {e}")
