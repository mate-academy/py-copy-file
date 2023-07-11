def copy_file(command: str) -> None:
    list_of_arguments_in_command = command.split()

    file_to_copy = list_of_arguments_in_command[1]
    file_copy = list_of_arguments_in_command[2]

    if file_to_copy != file_copy:
        with (open(file_to_copy, "r") as file_in,
             open(file_copy, "w") as file_out):
            file_out.write(file_in.read())
