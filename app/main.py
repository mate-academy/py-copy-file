import os


def copy_file(command: str) -> None:
    list_of_files = command.split(" ")
    if len(list_of_files) != 3 or list_of_files[0] != "cp":
        return
    _, old_file, new_file = list_of_files
    if old_file == new_file:
        return
    if not os.path.exists(old_file):
        return
    with (open(old_file, "r") as source_file_object,
          open(new_file, "w") as new_file_object):
        new_file_object.write(source_file_object.read())
