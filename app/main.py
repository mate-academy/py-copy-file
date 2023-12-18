class FileCopyError(Exception):
    """Raise when my source and target file are the same"""


class WrongCommandError(Exception):
    """Raise when user written wrong command name"""


class WrongArgumentsNumberError(Exception):
    """Raise when user command consists not from 3 elements"""


def copy_file(command: str) -> None:
    if len(command.split(" ")) != 3:
        raise WrongArgumentsNumberError("Your copy command "
                                        "should have 3 arguments!")
    cp_command, file_1, file_2 = command.split(" ")
    if file_1 == file_2:
        raise FileCopyError("Source and target file are the same!")
    elif cp_command != "cp":
        raise WrongCommandError("You written wrong command, "
                                "if you wanna copy file, use cp command")
    else:
        with open(file_1, "r") as source, open(file_2, "a") as target:
            target.write(source.read())
