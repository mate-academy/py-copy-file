def copy_file(command: str) -> None:
    command_name, file_name, new_name = command.split()
    if command_name == "cp" and file_name != new_name:
        with open(file_name, "r") as file_in, open(new_name, "w") as file_out:
            file_out.write(file_in.read())
