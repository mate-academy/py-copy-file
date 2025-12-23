def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) == 3:
        command_name, source_file, destination_file = parts
        if command_name == "cp" and not destination_file == source_file:
            command_name, source_file, destination_file = parts
            try:
                with (open(source_file)
                      as source_file,
                      open(destination_file, "w") as destination_file):
                    destination_file.write(source_file.read())
            except FileNotFoundError:
                return
