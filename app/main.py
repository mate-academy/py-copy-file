import shutil


def copy_file(command: str) -> None:
    command_split = command.split()
    if len(command_split) == 3 and command_split[0] == "cp":
        file_name_1, file_name_2 = command_split[1], command_split[2]
        if file_name_1 != file_name_2:
            shutil.copyfile(file_name_1, file_name_2)
    else:
        print("Invalid command. Usage: cp <source_file> <destination_file>")
