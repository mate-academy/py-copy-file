def copy_file(command: str) -> None:

    try:
        action, source, destination = command.split()
    except ValueError:
        return

    if action != "cp":
        return

    try:
        with open(source, "r") as file_in, open(destination, "w") as file_out:
            for line in file_in:
                file_out.write(line)

    except FileNotFoundError:
        return
