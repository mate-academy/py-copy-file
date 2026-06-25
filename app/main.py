def copy_file(command: str) -> None:
    command_list = command.split()

    if len(command_list) != 3 or command_list[0] != "cp":
        return

    source = command_list[1]
    destination = command_list[2]

    if source == destination:
        return

    try:
        with (open(source, "r") as source_file,
              open(destination, "w") as destination_file):
            destination_file.write(source_file.read())
    except FileNotFoundError:
        return
