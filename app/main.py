from shutil import copy


def copy_file(command: str) -> None:
    split_command = command.split(" ")

    source_file = split_command[1]
    destination_file = split_command[2]

    if source_file == destination_file:
        return

    copy(source_file, destination_file)
