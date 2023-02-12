def copy_file(command: str) -> None:
    command_type, source, destination = command.split()
    if command_type == "cp":
        with (
                open(source, "r") as file_in,
                open(destination, "w") as file_out
        ):
            result = file_in.read()
            file_out.write(result)
