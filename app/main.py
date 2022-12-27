def copy_file(command: str) -> None:
    command_type, source, destination = command.split()
    if command_type == "cp" and source != destination:
        with open(source, "r") as file_in, open(destination, "w") as file_out:
            file_out.write(file_in.read())
