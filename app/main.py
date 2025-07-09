def copy_file(command: str) -> None:
    command_list = command.strip().split()

    if not len(command_list) == 3:
        return
    action, source, destination = command_list

    if action != "cp" or source == destination:
        return

    try:
        with open(source, "r") as file_in, open(destination, "w") as file_out:
            for line in file_in:
                file_out.write(line)

    except FileNotFoundError:
        return
