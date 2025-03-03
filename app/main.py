def copy_file(command: str) -> None:
    split_command = command.split(" ")

    if len(split_command) != 3 or split_command[0] != "cp":
        return
    source, destination = split_command[1], split_command[2]
    if source == destination:
        return

    try:
        with open(source, "r") as file_in, open(destination, "w") as file_out:
            file_out.write(file_in.read())

    except FileNotFoundError:
        return
