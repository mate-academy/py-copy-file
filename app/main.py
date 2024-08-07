def copy_file(command: str) -> None:
    if len(command.split()) == 3:
        commands, source_file, destination_file = command.split()
        if commands == "cp" and source_file != destination_file:
            with (
                open(
                    f"{source_file}", "r"
                ) as first_file,
                open(
                    f"{destination_file}", "w"
                ) as copy_file
            ):
                copy_file.write(first_file.read())
