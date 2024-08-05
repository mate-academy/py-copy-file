def copy_file(command: str) -> None:
    if command.split()[1] != command.split()[2]:
        with (open(
                f"{command.split()[1]}",
                "r"
        ) as first_file,
            open(
                f"{command.split()[2]}",
                "w"
        ) as copy_file):
            copy_file.write(first_file.read())
