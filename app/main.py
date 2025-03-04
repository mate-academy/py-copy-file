import os


def copy_file(command: str) -> None:
    command_ls = command.split(" ")
    cp_check = command_ls[0]

    if cp_check != "cp":
        return None

    if len(command_ls) != 3:
        return None

    first_file = command_ls[1]
    second_file = command_ls[2]

    if not os.path.exists(first_file):
        return None

    if first_file == second_file:
        return None

    with open(first_file, "r") as first, open(second_file, "w") as second:
        for line in first:
            second.write(line)
