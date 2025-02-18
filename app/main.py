def copy_file(command: str) -> None:
    source = command.split()
    if len(source) != 3 and source[0] != "cp":
        return
    if source[1] == source[2]:
        return

    try:
        with (
            open(source[1], "r") as file_from,
            open(source[2], "w") as file_to
        ):
            file_to.write(file_from.read())
    except FileNotFoundError as error:
        print(error)
