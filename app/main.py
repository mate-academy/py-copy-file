class EqualNamesError(Exception):
    pass


def copy_file(command: str) -> None:
    command, file, new_file = command.split()

    if file == new_file:
        raise EqualNamesError("File names have not to be equal!!!")

    elif command == "cp":
        with open(file, "r") as \
                old_file, open(new_file, "w") as new_file:
            read_file = old_file.read()
            new_file.write(read_file)
