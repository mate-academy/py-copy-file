from shutil import copyfileobj


def copy_file(command: str) -> None:
    parts = command.split()
    command, source_filename, destination_filename = parts
    if all([len(parts) == 3, command == "cp",
            source_filename != destination_filename]):

        with (open(source_filename, "r") as source,
              open(destination_filename, "w") as destination):
            copyfileobj(source, destination)
