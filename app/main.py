def copy_file(command_line: str) -> None:
    _, source_name, destination_name = command_line.split(" ")

    if source_name == destination_name:
        return

    with (open(source_name, "r") as source,
          open(destination_name, "w") as destination):

        destination.writelines(source.readlines())
