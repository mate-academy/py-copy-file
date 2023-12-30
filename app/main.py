import shutil


def copy_file(command: str) -> None:
    command_file = command.split()

    if len(command_file) != 3 or command_file[0] != "cp":
        print("Wrong command!")

    src_f = command_file[1]
    dest_f = command_file[2]
    if src_f != dest_f:
        shutil.copy2(src_f, dest_f)
