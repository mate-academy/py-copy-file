def copy_file(command: str) -> None:
    command_parts = command.split(" ")
    command = command_parts[0]
    source_file_name = command_parts[1]
    destination_file_name = command_parts[2]
    if command != "cp" or source_file_name == destination_file_name:
        return

    with (open(source_file_name, "r") as source,
         open(destination_file_name, "w") as destination):
        destination.write(source.read())
