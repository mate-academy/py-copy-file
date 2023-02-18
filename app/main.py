from app.error import WrongCommandError, SameNameError, ArgumentsError


def copy_file(command: str) -> None:

    command = command.split(" ")

    if command[0] != "cp":
        raise WrongCommandError("Incorrect command")

    if command[1] == command[2]:
        raise SameNameError("The copy should be renamed")

    if len(command) != 3:
        raise ArgumentsError(
            "'Command', 'file name' and 'new file' name should be provided"
        )

    with open(command[1], "r") as file_in, open(command[2], "w") as file_out:
        file_out.write(file_in.read())
