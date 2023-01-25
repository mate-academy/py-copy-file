def copy_file(command: str) -> None:
    splitted = command.split()
    if len(splitted) == 3:
        if splitted[0] == "cp" and splitted[1] != splitted[2]:
            with (
                open(splitted[1], "r") as source_file,
                open(splitted[2], "w") as target_file
            ):
                target_file.write(source_file.read())
