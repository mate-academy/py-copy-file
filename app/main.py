def copy_file(command: str) -> None:
    command_list = command.split()

    if len(command_list) != 3 or command_list[0] != "cp":
        return

    _, source_file, destination_file = command_list
    if source_file == destination_file:
        return

    with (open(
            source_file, "rb") as file_to_copy,
            open(destination_file, "wb") as file_after_copy):
        file_after_copy.write(file_to_copy.read())
