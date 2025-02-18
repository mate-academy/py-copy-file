def copy_file(command: str) -> None:
    command, source_file, destination_file = command.split()
    if command == "cp" and source_file != destination_file:
        with (
            open(f"{source_file}", "r") as file_in,
            open(f"{destination_file}", "w") as file_out
        ):
            file_out.write(file_in.read())
