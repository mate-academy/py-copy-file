def copy_file(command: str) -> None:
    if len(command) == 2:
        current_command, source_file, destination_file = command.split()
        if source_file != destination_file:
            with open(source_file) as source_file, \
                    open(destination_file, "w") as destination_file:

                content = source_file.read()
                destination_file.write(content)
