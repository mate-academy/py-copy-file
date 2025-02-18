def copy_file(command: str) -> None:
    parts = command.split()

    if len(parts) == 3:
        cmd, source_file, destination_file = parts
        if cmd == "cp" and source_file != destination_file:

            with (
                open(source_file, "r") as file_in,
                open(destination_file, "w") as file_out
            ):
                file_out.write(file_in.read())
