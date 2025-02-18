def copy_file(command: str) -> None:
    list_command = command.split()
    if len(list_command) == 3:
        source_file, destination_file = list_command[1], list_command[2]
        if source_file != destination_file:
            with (
                open(source_file, "r") as file_in,
                open(destination_file, "w") as file_out
            ):
                file_out.write(file_in.read())
