class WrongCommandError(Exception):
    pass


def copy_file(command: str) -> None:
    try:
        action, file_to_copy, new_file = command.split()
        if action != "cp":
            raise WrongCommandError
    except ValueError:
        print(
            "The command should contain cp "
            "and names of two files separated by spaces"
        )
        raise
    except WrongCommandError:
        print("The command should start with cp")
        raise

    if file_to_copy == new_file:
        return
    try:
        with (
            open(file_to_copy, "r") as file_in,
            open(new_file, "w") as file_out
        ):
            file_out.write(file_in.read())
    except FileNotFoundError:
        print(
            "The files names should be correct "
            "and the files should exist in the current directory"
        )
        raise
