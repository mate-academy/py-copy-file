import os


def copy_file(command: str) -> None:
    command_split = command.split()
    if (len(command_split) == 3
            and "cp" in command_split[0]
            and command_split[1].endswith(".txt")
            and command_split[2].endswith(".txt")
            and command_split[1] != command_split[2]
            and os.path.exists(command_split[1])):
        with (open(command_split[1], "r") as file_in,
              open(command_split[2], "w") as file_out):
            content = file_in.read()
            file_out.write(content)
