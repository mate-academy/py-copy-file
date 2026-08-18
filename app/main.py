from pathlib import Path


def copy_file(command: str) -> None:
    command_list = command.split()
    if len(command_list) != 3:
        return
    command_name, source, destination = command_list
    if command_name == "cp" and Path(source).exists():
        with (open(source) as file_from,
              open(destination, "w") as file_to):
            file_to.write(file_from.read())
