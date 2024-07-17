def copy_file(command: str) -> None:
    _, copy_from, copy_to = command.split()
    if copy_from == copy_to:
        return

    with (
        open(copy_from, "r") as starting_file,
        open(copy_to, "w") as destination_file
    ):
        destination_file.write(
            starting_file.read()
        )
