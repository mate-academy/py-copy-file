def copy_file(command: str) -> None:
    input_command, file_name_to_copy, new_file_name = command.split()

    if input_command == "cp" and file_name_to_copy != new_file_name:
        with (open(file_name_to_copy, "r") as file_in,
                open(new_file_name, "w") as file_out):
            file_out.write(file_in.read())
