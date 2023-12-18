def copy_file(command: str) -> None:
    splitted_arguments = command.split()
    if len(splitted_arguments) != 3:
        raise ValueError("Incorrect command provided")
    command, file_name_to_copy, new_file_name = splitted_arguments

    if command != "cp" or file_name_to_copy == new_file_name:
        raise ValueError("Incorrect command provided")

    with open(file_name_to_copy, "r") as file_in, \
            open(new_file_name, "w") as file_out:
        file_out.write(file_in.read())
