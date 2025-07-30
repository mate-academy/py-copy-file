def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3:
        return

    copy_command, source, destination = parts
    if copy_command == "cp" and source != destination:
        try:
            with (
                open(source, "r")
                as source_file, open(destination, "w")
                as destination_file
            ):

                content = source_file.read()
                destination_file.write(content)
        except FileNotFoundError:
            pass
