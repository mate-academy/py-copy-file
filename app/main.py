def copy_file(command: str) -> None:
    command_name, file_name, new_file_name = command.split()
    if command == "cp" and file_name != new_file_name:
        with (
            open(f"{file_name}", "r") as file_in,
            open(f"{new_file_name}", "w") as file_out
        ):
            file_out.write(file_in.read())
