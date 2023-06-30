import os


def copy_file(command: str) -> None:
    command_list = command.split(" ")
    if command_list[0] == "cp" and command_list[1] != command_list[2] and os.path.exists(command_list[1]):
        with (open(command_list[1], "r") as file_in,
              open(command_list[2], "w") as file_out):
            text = file_in.read()
            file_out.write(text)
