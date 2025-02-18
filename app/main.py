def copy_file(command: str) -> None:
    if not command.startswith("cp "):
        raise ValueError("Command must start with 'cp '")

    parts = command.split()

    if len(parts) != 3:
        raise ValueError("Invalid command format. "
                         "Use: cp source_file destination_file")

    source_file, destination_file = parts[1], parts[2]

    if source_file == destination_file:
        return

    with (open(source_file, "r") as file_in,
          open(destination_file, "w") as file_out):
        file_out.write(file_in.read())
