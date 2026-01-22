def copy_file(command: str) -> None:
    copy_command, name, new_name = command.split()
    if new_name != name:
        with open(name, "r") as file_in, open(new_name, "w") as file_out:
            file_out.write(file_in.read())
