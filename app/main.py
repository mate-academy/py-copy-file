class UnidentifiedCommandError(Exception):
    pass


def copy_file(command: str) -> None:
    cm, copy_filename, new_filename = command.split()
    if cm != "cp":
        try:
            raise UnidentifiedCommandError
        except UnidentifiedCommandError as error:
            print(error, "You need to type correct command.")

    if copy_filename != new_filename:
        try:
            with (
                open(copy_filename, "r") as copy,
                open(new_filename, "w") as new
            ):
                new.write(copy.read())
        except FileNotFoundError:
            print("No such file in the directory")
