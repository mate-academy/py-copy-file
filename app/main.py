def copy_file(command: str) -> None:
    command, file_read, file_write = command.split()
    if command == "cp" and file_read != file_write:
        with (
            open(f"{file_read}", "r") as file_in,
            open(f"{file_write}", "w") as file_out
        ):
            file_out.write(file_in.read())
