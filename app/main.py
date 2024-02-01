def copy_file(command: str) -> None:
    commands_list = command.split()
    if len(commands_list) == 3:
        cp_command, source_name, destination_name = commands_list
        if source_name != destination_name and cp_command == "cp":
            with (open(source_name, "r") as source,
                  open(destination_name, "w") as destination):
                destination.write(source.read())
