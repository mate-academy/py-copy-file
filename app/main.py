from shutil import copyfileobj


def copy_file(command: str) -> None:
    parts = command.split()
    source_filename, destination_filename = parts[1], parts[2]
    if (len(parts) == 3 and parts[0] == "cp"
            and source_filename != destination_filename):

        with (open(source_filename, "r") as source,
              open(destination_filename, "w") as destination):
            copyfileobj(source, destination)
