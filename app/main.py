def copy_file(command: str) -> None:
    if command.split()[1] == command.split()[2]:
        return None

    with (
        open(command.split()[1], "r") as origin,
        open(command.split()[2], "w") as copy
    ):
        copy.write(origin.read())
