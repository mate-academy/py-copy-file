def copy_file(command: str) -> None:
    try:
        command, source_file, target_file = command.split(maxsplit=3)
    except ValueError:
        raise ValueError("Command must have 'cp' keyword and 2 arguments")

    if command == "cp" and source_file != target_file:
        with (
                open(source_file, "r") as source,
                open(target_file, "w") as target
        ):
            target.write(source.read())
