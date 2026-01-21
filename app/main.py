def copy_file(command: str) -> None:
    command, source_filepath, destination_filepath = command.split()
    if source_filepath != destination_filepath and command == "cp":
        with open(source_filepath, "r") as file_in, \
                open(destination_filepath, "w") as file_out:
            file_out.write(file_in.read())
