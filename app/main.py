from pathlib import Path


def copy_file(command: str) -> None:
    command_list = command.split()
    if ("cp" in command_list
            and len(command_list) == 3
            and Path(command_list[1]).exists()):
        with (open(command_list[1]) as file_from,
              open(command_list[2], "w") as file_to):
            file_to.write(file_from.read())
