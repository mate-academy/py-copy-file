def copy_file(command: str) -> None:
    _, file_to_copy, file_copied = command.split()
    if file_to_copy == file_copied:
        return

    with (
        open(file_to_copy, "r") as file_in,
        open(file_copied, "w") as file_copy
    ):
        file_copy.write(file_in.read())
