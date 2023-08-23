def copy_file(command: str) -> None:
    command, source_file, copied_file = command.split()
    if source_file == copied_file or command != "cp":
        return
    with open(source_file, "r") as sourse:
        with open(copied_file, "w") as copy:
            copy.write(sourse.read())
