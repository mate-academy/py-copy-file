import os


def copy_file(command: str) -> None:
    command_list = command.split()
    if len(command_list) < 3:
        return
    elif command_list[0] != "cp":
        return
    elif command_list[1] == command_list[2]:
        return
    elif os.path.isfile(command_list[1]):
        with (open(command_list[1], "r") as file_in,
              open(command_list[2], "w") as file_out):
            file_out.write(file_in.read())
