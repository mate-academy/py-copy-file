import os


def copy_file(command: str) -> str:
    command_line = command.split()

    if command_line == []:
        return ""

    if len(command_line) < 3:
        return ""

    if (command_line[0] == "cp"
            and command_line[1] != command_line[2]
            and os.path.exists(command_line[1])):
        with (open(command_line[1], "r") as file_in,
              open(command_line[2], "w") as file_out):
            file_out.write(file_in.read())
