def copy_file(command: str) -> None:
    if not command:
        return

    command_list: list[str] = command.split()

    if len(command_list) != 3:
        return

    if command_list[0] != "cp":
        return

    source_file: str = command_list[1]
    destination_file: str = command_list[2]

    if source_file == destination_file:
        return

    try:
        with (open(source_file, "r") as file_in,
              open(destination_file, "w") as file_out):
            content = file_in.read()
            file_out.write(content)

    except FileNotFoundError:
        return
