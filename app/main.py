import shlex


def copy_file(command: str) -> None:
    commands = shlex.split(command)
    source_file = commands[1]
    destination_file = commands[2]

    if commands[0] == "cp" or source_file != destination_file:
        with open(source_file, "r") as read_file, \
                open(destination_file, "x") as write_file:
            write_file.writelines(read_file.readlines())
