import shutil
import os


def copy_file(command):

    split_command = command.split()

    if len(split_command) != 3 or split_command[0] != "cp":
        return

    source_filename, target_filename = split_command[1], split_command[2]

    if os.path.exists(source_filename) and source_filename != target_filename:
        shutil.copyfile(source_filename, target_filename)
    else:
        return
