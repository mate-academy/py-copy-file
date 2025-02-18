def copy_file(command: str) -> None:
    command = command.split()
    if command[0] == "cp" and command[1] != command[2]:
        with (
            open(command[1]) as file_read,
            open(command[2], "w") as file_write
        ):
            file_write.write(file_read.read())
