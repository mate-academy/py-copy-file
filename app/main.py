def copy_file(command: str) -> None:
    command_name, file, file_to_copy = command.split()
    if command_name == "cp" and file != file_to_copy:
        try:
            with (open(file, "r") as current_file,
                  open(file_to_copy, "w") as new_file):
                new_file.write(current_file.read())
        except FileNotFoundError as found_error:
            print(found_error)
            return
