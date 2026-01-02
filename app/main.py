def copy_file(command: str) -> str:
    parts = command.split()

    if len(parts) != 3:
        return "Invalid command format"

    command_name, source_file, destination_file = parts

    if command_name != "cp":
        return "Invalid command"

    if source_file == destination_file:
        return "Source and destination files are the same"

    with (open(source_file) as source,
          open(destination_file, "wt") as destination):
        destination.write(source.read())

    return f"File {source_file} copied to {destination_file}"
