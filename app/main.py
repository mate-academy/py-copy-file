import os


def copy_file(command: str) -> None:
    copy_list = command.strip().split()
    if len(copy_list) != 3 or copy_list[0] != "cp":
        return None
    source_file_name = copy_list[1]
    if not os.path.exists(source_file_name):
        return None
    destination_file_name = copy_list[-1]
    if source_file_name == destination_file_name:
        return None
    with (open(source_file_name, "r") as source_file,
          open(destination_file_name, "w") as destination_file):
        destination_file.write(source_file.read())
