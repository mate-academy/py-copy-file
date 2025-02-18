def copy_file(command: str) -> None:
    command = command.split()

    if len(command) != 3:
        raise ValueError("Use cp command, file source, file destination")

    command_cp, file_source, file_destination = command

    if file_source != file_destination and command_cp == "cp":
        try:
            with (
                open(file_source) as file_in,
                open(file_destination, "w") as file_out
            ):
                file_out.write(file_in.read())
        except FileNotFoundError:
            print(f"File {file_source} does not exist")
