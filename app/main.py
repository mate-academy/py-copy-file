import os


def copy_file(command: str) -> None:
    command_list = command.split()
    if len(command_list) != 3 or command_list[0] != "cp":
        return
    source_file_name = command_list[1]
    destination_file_name = command_list[2]
    if source_file_name == destination_file_name:
        return
    if not os.path.exists(source_file_name):
        return
    with (open(source_file_name, "r") as file_src,
          open(destination_file_name, "w") as file_cp):
        file_cp.write(file_src.read())
