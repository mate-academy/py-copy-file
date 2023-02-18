from shutil import copyfile


def copy_file(command: str) -> None:
    execution_command, curr_file, new_file = command.split(" ")

    if execution_command == "cp" and curr_file != new_file:
        copyfile(curr_file, new_file)
