def copy_file(command: str) -> None:
    arguments = command.split()

    if len(arguments) != 3:
        return

    command, file_from_name, file_to_name = arguments

    if command != "cp" or file_to_name == file_from_name:
        return

    try:
        with (
            open(file_from_name, "r", encoding="utf-8") as file_from,
            open(file_to_name, "w", encoding="utf-8") as file_to
        ):
            file_to.write(file_from.read())
    except FileNotFoundError:
        return
