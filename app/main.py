def copy_file(command: str) -> None:
    if len(command.split()) != 3:
        raise ValueError(
            "Invalid command. "
            "Expected three parts: mode, source file, destination file."
        )
    mode, source_file, destination_file = command.split()
    if mode == "cp" and source_file != destination_file:
        with open(source_file, "r") as file_in, \
                open(destination_file, "w") as file_out:
            file_out.write(file_in.read())
