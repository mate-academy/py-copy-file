from shutil import copyfile


def copy_file(command: str) -> None:
    execution_command, current_file, new_file = command.split()

    if execution_command == "cp" and current_file != new_file:
        copyfile(current_file, new_file)
