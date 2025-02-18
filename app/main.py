def copy_file(command: str) -> None:
    cur_command, original_file, copy_file = command.split()
    if command == "cp" and original_file != copy_file:
        with (
            open(original_file, "r") as file_in,
            open(copy_file, "w") as file_out
        ):
            file_out.write(file_in.read())
