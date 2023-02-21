def copy_file(command: str) -> None:
    copy_command, original_file, duplicate_file = command.split()
    if original_file != duplicate_file:
        with open(original_file, "r") as file_in, \
             open(duplicate_file, "w") as file_out:
            file_out.write(file_in.read())
