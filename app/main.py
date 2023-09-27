from shutil import copyfileobj


def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3:
        return

    cp, source_file, destination_file = parts
    if source_file == destination_file:
        return

    with (open(source_file, "r") as source,
          open(destination_file, "w") as destination):
        copyfileobj(source, destination)
