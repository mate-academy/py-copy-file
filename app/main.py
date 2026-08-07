from os.path import exists


def copy_file(command: str) -> None:
    file_list = command.split(" ")

    if len(file_list) != 3:
        return
    if file_list[0] != "cp":
        return
    if not exists(file_list[1]):
        return
    if file_list[1] == file_list[2]:
        return

    with (open(file_list[1], "r") as file_in,
          open(file_list[2], "w") as file_out):
        file_out.write(file_in.read())
