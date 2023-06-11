def copy_file(command: str) -> None:
    command = command.split()
    cp, source_file, destination_file = command
    if source_file != destination_file and cp == "cp":
        with open(source_file, "r") as file_in,\
                open(destination_file, "w") as file_out:
            file_out.write(file_in.read())
