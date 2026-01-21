def copy_file(command: str) -> None:
    if len(command.split()) == 3 and command.split()[0] == "cp":
        cp, file_read, file_write = command.split()

        if file_read == file_write:
            return
        with (
            open(file_read, "r") as file_in,
            open(file_write, "w") as file_out
        ):
            file_out.write(file_in.read())
