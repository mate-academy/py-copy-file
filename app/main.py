import os


def copy_file(command: str) -> None:
    array = command.split(" ")

    if len(array) != 3:
        return

    arg1, arg2, arg3 = array

    if arg1 != "cp" or arg2 == arg3:
        return

    if not os.path.exists(arg2):
        return

    with open(arg2, "r") as file_in, open(arg3, "w") as file_out:
        data = file_in.read()
        file_out.write(data)
