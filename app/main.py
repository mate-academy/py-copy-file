def copy_file(command: str) -> None:
    source_file = command.split()[1]
    destination_file = command.split()[2]
    with (open(source_file, "r") as source_file,
          open(destination_file, "w") as destination_file):
        destination_file.write(source_file.read())
