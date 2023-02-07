def copy_file(command: str) -> None:
    file_copied = command.split()
    if file_copied[1] == file_copied[2]:
        return

    with (
        open(file_copied[1], "r") as file_in,
        open(file_copied[2], "w") as file_copy
    ):
        file_copy.write(file_in.read())
