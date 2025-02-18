def copy_file(command: str) -> None:
    parts = command.split()
    if (
        len(parts) == 3
        and parts[0] == "cp"
        and parts[1] != parts[2]
    ):
        with (
            open(parts[2], "w") as new_file,
            open(parts[1], "r") as old_file
        ):
            new_file.write(old_file.read())
