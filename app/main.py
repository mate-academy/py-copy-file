def copy_file(command: str) -> None:
    cp_command, file_name, new_file_name = command.split()

    if cp_command != "cp" or file_name == new_file_name:
        return

    with open(file_name, "r") as file_in, open(new_file_name, "w") as file_out:
        file_out.write(file_in.read())
