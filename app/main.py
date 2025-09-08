from pathlib import Path


def copy_file(command: str) -> None:
    command_parts = command.split()

    if len(command_parts) != 3:
        return

    if command_parts[0] == "cp":

        if command_parts[1] == command_parts[2]:
            return

        source_file_name = command_parts[1]
        destination_file_name = command_parts[2]

        if not Path(source_file_name).is_file():
            return

        with (open(source_file_name, "r") as source_file_object,
              open(destination_file_name, "w") as destination_file_object):
            destination_file_object.write(source_file_object.read())
