def copy_file(command: str) -> None:
    cp_command, source_file, copied_file = command.split()

    if cp_command == "cp" and source_file == copied_file:
        return

    with open(source_file, "r") as source, open(copied_file, "w") as copied:
        copied.write(source.read())
