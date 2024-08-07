
def copy_file(command: str) -> None:
    new_str = command.split(" ", 2)
    cmd, file_first, file_second = new_str

    if len(new_str) == 3 and file_first != file_second and cmd == "cp":

        try:
            with (
                open(file_first, "r") as first,
                open(file_second, "w") as second
            ):
                second.write(first.read())
        except OSError as e:
            print(f"Error {e}")
