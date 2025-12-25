class FileError(Exception):
    pass


def copy_file(command: str) -> None:
    is_cp, command_to_read, command_to_write = command.split()

    if is_cp == "cp" and command_to_read != command_to_write:
        try:
            with (
                open(command_to_read, "r") as file_in,
                open(command_to_write, "w") as file_out
            ):
                file_out.write(file_in.read())
        except FileError:
            print("The file is corrupted")
