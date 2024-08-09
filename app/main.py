def copy_file(command: str) -> None:
    parts = command.split()

    if (
        len(parts) == 3
        and parts[0] == "cp"
        and parts[1] == parts[2]
    ):
        _, source_file, destination_file = parts

    try:
        with (
            open(source_file, "r") as file_in,
            open(destination_file, "w") as file_out
        ):

            file_out.write(file_in.read())

    except OSError:
        print("An error occured")
