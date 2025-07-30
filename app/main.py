def copy_file(command: str) -> None:
    parts = command.split()
    _, source, destination = parts
    with open(source, "r") as source_file, open(destination, "w") as destination_file:
        content = source_file.read()
        destination_file.write(content)
