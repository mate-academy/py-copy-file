def copy_file(command: str) -> None:

    try:
        action, source, destination = command.strip().split()
    except ValueError:
        return

    if action != "cp" or source == destination:
        return

    try:
        with open(source, "r") as file_in, open(destination, "w") as file_out:
            for line in file_in:
                file_out.write(line)

    except FileNotFoundError:
        return
