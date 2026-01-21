def copy_file(command: str) -> None:
    command, current_file_name, new_file_name = command.split()
    if current_file_name != new_file_name and command == "cp":
        with (
            open(current_file_name, "r") as current_file,
            open(new_file_name, "w") as new_file
        ):
            new_file.write(current_file.read())
