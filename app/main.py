from pathlib import Path


def copy_file(full_command: str) -> None:
    command_list = full_command.split()
    if len(command_list) != 3:
        return

    if command_list[0] != "cp":
        return

    source_path = command_list[1]
    destination_path = command_list[2]

    if not Path(source_path).is_file():
        return

    if source_path == destination_path:
        return

    with (open(source_path, "r") as file_from,
          open(destination_path, "w") as file_to):
        file_to.write(file_from.read())
