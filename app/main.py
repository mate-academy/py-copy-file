def copy_file(command: str) -> None:
    try:
        trash, source, destination = command.split()
    except ValueError:
        return
    if trash != "cp" or not source or not destination:
        return
    if source == destination:
        return
    try:
        with open(
            source, "r"
        ) as source_file, open(
            destination, "w"
        ) as destination_file:
            for line in source_file:
                destination_file.write(line)
    except FileNotFoundError:
        return
