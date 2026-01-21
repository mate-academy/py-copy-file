import os


def copy_file(command: str) -> None:
    name_list = command.split(" ")

    if len(name_list) != 3 or name_list[0] != "cp":
        return

    file_name = name_list[1]
    new_file_name = name_list[2]

    if file_name == new_file_name:
        return

    if not os.path.exists(file_name):
        return

    with open(file_name, "r") as file_in, open(new_file_name, "w") as file_out:
        for line in file_in:
            file_out.write(line)
