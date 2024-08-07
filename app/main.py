def copy_file(command: str) -> None:
    try:
        parts = command.split()

        if (
                len(parts) != 3
                or parts[0] != "cp"
                or parts[1] == parts[2]
        ):
            return

        source_file = parts[1]
        destination_file = parts[2]

        with (
            open(source_file, "r") as file_in,
            open(destination_file, "w") as file_out
        ):
            file_out.write(file_in.read())

    except Exception as e:
        raise OSError("An error occurred") from e
