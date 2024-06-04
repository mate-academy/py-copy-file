def copy_file(command: str) -> None:
    parts = command.split()
    if parts[0] == "cp" and len(parts) == 3 and parts[1] == parts[2]:
        with (
            open(parts[1], "r") as file_read,
            open(parts[2], "w") as file_write
        ):
            file_write.write(file_read.read())
