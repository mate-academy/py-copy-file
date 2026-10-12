import os


def copy_file(command: str) -> None:
    command_list = command.split(" ")

    if len(command_list) != 3 or command_list[0] != "cp":
        return

    if (command_list[1] == command_list[2]
            or not os.path.exists(command_list[1])):
        return

    with (open(f"{command_list[1]}", "r") as file_in,
          open(f"{command_list[2]}", "w") as file_out):
        for line in file_in:
            file_out.write(line)
