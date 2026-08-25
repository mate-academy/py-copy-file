import os


def copy_file(command: str) -> None:
    command_splited = command.split()
    if len(command_splited) < 3:
        return
    old_file = command_splited[1]
    new_file = command_splited[2]
    if (old_file == new_file
            or not os.path.exists(old_file)
            or command_splited[0] != "cp"):
        return

    with open(old_file, "r") as file_in, open(new_file, "w") as file_out:
        file_out.write(file_in.read())
