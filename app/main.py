def copy_file(command: str) -> None:
    command_name, source_file, destination_file, *_ = command.split()
    if command_name != "cp":
        raise ValueError(
            "Invalid command format."
            "Expected format: cp source_file destination_file"
        )
    if source_file == destination_file:
        raise ValueError(
            "The source file and the destination file have the same names."
        )
    with open(source_file, "r") as file_in:
        with open(destination_file, "w") as file_out:
            file_out.write(file_in.read())
