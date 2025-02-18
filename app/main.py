def copy_file(copy_command: str) -> None:
    cmd, file_name, new_file_name = copy_command.split()
    if cmd == "cp" and file_name != new_file_name:
        with (
            open(file_name, "r") as file_in,
            open(new_file_name, "w") as file_out
        ):
            file_out.write(file_in.read())
