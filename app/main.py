def copy_file(command: str) -> None:
    cmd, source_file, second_file = command.split()
    if source_file == second_file or cmd != "cp":
        return
    with (
        open(source_file, "r") as source,
        open(second_file, "w") as second
    ):
        second.write(source.read())
