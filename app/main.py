def copy_file(command: str) -> None:
    cp_command, source_name, destination_name = command.split()
    if source_name != destination_name and cp_command == "cp":
        with (open(source_name, "r") as source,
              open(destination_name, "w") as destination):
            destination.write(source.read())
