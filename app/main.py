import os


def copy_file(string: str) -> str:
    command = string.split()

    if command == []:
        return ""

    if len(command) < 3:
        return ""

    if (command[0] == "cp"
            and command[1] != command[2]
            and os.path.exists(command[1])):
        with (open(command[1], "r") as file_in,
              open(command[2], "w") as file_out):
            file_out.write(file_in.read())
