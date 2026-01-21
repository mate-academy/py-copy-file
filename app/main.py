def copy_file(command: str) -> None:
    command_split = command.split(" ")
    if len(command_split) == 3 and command_split[0] == "cp":
        source_file_name = command_split[1]
        destination_file_name = command_split[2]
        if source_file_name != destination_file_name:
            with (open(source_file_name, "r") as file_to_copy,
                  open(destination_file_name, "w") as file_copy):
                file_copy.write(file_to_copy.read())
