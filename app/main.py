import os


def copy_file(command: str) -> None:
    command = command.split()
    if len(command) != 3:
        return
    if command[0] != "cp":
        return
    command_old_file = command[1]
    command_new_file = command[2]
    if command_old_file == command_new_file:
        return
    if not os.path.exists(command_old_file):
        return
    with (open(command_old_file, "r") as file_in,
          open(command_new_file, "w") as file_out):
        info_old_file = file_in.read()
        file_out.write(info_old_file)
