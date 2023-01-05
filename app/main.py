def copy_file(command: str) -> None:
    command, file_name, new_file_name = command.split()
    if command == "cp" and file_name != new_file_name:
        with (
            open(file_name, "r") as file_in,
            open(new_file_name, "w") as file_out
        ):
            file_out.write(file_in.read())
