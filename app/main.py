def copy_file(command: str) -> None:
    parts = command.split()

    if parts[0] == "cp" and len(parts) == 3 and parts[1] != parts[2]:
        source_file, destination_file = parts[1], parts[2]

        with (
            open(source_file, "r") as file_in,
            open(destination_file, "w") as file_out
        ):
            file_out.write(file_in.read())
