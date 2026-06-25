def copy_file(command: str) -> None:
    file_parts = command.split()

    if len(file_parts) != 3:
        return

    action = file_parts[0]
    source_file = file_parts[1]
    destination_file = file_parts[2]

    if action != "cp":
        return

    if source_file == destination_file:
        return

    try:
        with (open(source_file, "r") as file_in,
              open(destination_file, "w") as file_out):
            file_out.write(file_in.read())
    except FileNotFoundError:
        return
