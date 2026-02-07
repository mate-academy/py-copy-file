def copy_file(command: str) -> None:

    command_parts = command.split()
    if len(command_parts) == 3:
        operation, source_file, destination_file = command_parts
        if source_file != destination_file and operation == "cp":
            try:
                with (open(source_file, "r") as file_in,
                      open(destination_file, "w") as file_out):
                    file_out.write(file_in.read())
            except FileNotFoundError:
                return None
    return None
