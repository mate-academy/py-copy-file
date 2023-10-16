def copy_file(command: str) -> None:
    cp, file_name_to_copy, new_file_name = command.split()

    if cp == "cp" and file_name_to_copy != new_file_name:
        with (open(file_name_to_copy) as file_to_copy,
             open(new_file_name, "w") as new_file):
            new_file.writelines(file_to_copy.readlines())
