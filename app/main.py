def copy_file(command: str) -> None:
    source, destination = command.split()[1:]
    if source == destination:
        return
    with open(source, "r") as source_file,\
         open(destination, "w") as destination_file:
        destination_file.write(source_file.read())
