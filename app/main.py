def copy_file(command: str) -> None:
    command_alias, file_name_to_copy, new_file_name = command.split()

    if command_alias == "cp" and file_name_to_copy != new_file_name:
        with (open(file_name_to_copy) as file_to_copy,
             open(new_file_name, "w") as new_file):
            new_file.write(file_to_copy.read())
