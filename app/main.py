def copy_file(command: str) -> None:
    input_command, file_name_to_copy, new_file_name = command.split()
    if input_command != "cp" or file_name_to_copy == new_file_name:
        return

    with open(file_name_to_copy, "r") as file_in,\
            open(new_file_name, "w") as file_out:
        read_content = file_in.read()
        file_out.write(read_content)
