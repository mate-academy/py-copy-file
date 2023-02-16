import shutil
from typing import Any
from app.errors import (
    IncorrectCommand,
    IncorrectCopyCommand,
    IncorrectSecondFilename,
    FileNotExists
)
from app.validator import command_validator


def copy_file(command: str) -> Any:
    inner_command = command.split()
    try:
        command_validator(inner_command)
    except IncorrectCommand:
        print("Incorrect input of command in general")
    except IncorrectCopyCommand:
        print("Incorrect command for copying")
    except FileNotExists:
        print("The file to copy does not exist")
    except IncorrectSecondFilename:
        print("Input a new name for the file")
    else:
        with open(f"{inner_command[1]}", "r") as file_1:
            shutil.copyfile(f"{file_1.name}", f"{inner_command[2]}")
        print("File copying is complete!")
