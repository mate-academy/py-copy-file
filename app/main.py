import os


def copy_file(command: str) -> None:

    command_list = command.split()
    if len(command_list) == 3:
        cmd, file_in, file_out = command_list
    else:
        print("The command line should contain 3 commands ...")
        return

    path_in = os.path.join(os.path.dirname(__file__), file_in)
    path_out = os.path.join(os.path.dirname(__file__), file_out)

    if cmd != "cp":
        print("Enter correct command, please ...")
        return

    if file_in == file_out:
        print("Doing nothing ...")
        return

    with open(path_in, "r") as src, open(path_out, "w") as dst:
        dst.write(src.read())
