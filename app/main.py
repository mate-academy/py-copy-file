import shutil


def copy_file(command: str) -> None:
    command_list = command.split()
    if len(command_list) != 3:
        return
    if command_list[0] != "cp":
        return
    if command_list[1] != command_list[2]:
        try:
            shutil.copy(command_list[1], command_list[2])
        except FileNotFoundError:
            return
