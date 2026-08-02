import os


def copy_file(command: str) -> None:
    str_2_list = command.split()

    if len(str_2_list) != 3:
        return

    if str_2_list[0] != "cp":
        return

    source_file = str_2_list[1]
    dest_file = str_2_list[2]

    if not os.path.exists(source_file):
        return

    if source_file == dest_file:
        return

    with (
        open(str_2_list[1], "r")
        as file_in, open(str_2_list[2], "w")
        as file_out
    ):
        content = file_in.read()
        file_out.write(content)
