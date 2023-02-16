import os
from app.errors import (
    IncorrectCommand,
    IncorrectCopyCommand,
    IncorrectSecondFilename,
    FileNotExists
)


def command_validator(command: list) -> None:
    if len(command) != 3:
        raise IncorrectCommand("Incorrect input of command in general")
    if command[0] != "cp":
        raise IncorrectCopyCommand("Incorrect command for copying")
    if not os.path.isfile(command[1]):
        raise FileNotExists("The file to copy does not exist")
    if command[1] == command[2]:
        raise IncorrectSecondFilename("Same file names")
