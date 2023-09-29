def copy_file(command: str) -> None:
    try:
        cmd, source_file, second_file = command.split(maxsplit=3)
    except ValueError:
        raise
    if command == "cp" and source_file != second_file:
        with (
            open(source_file, "r") as source,
            open(second_file, "w") as second
        ):
            second.write(source.read())
