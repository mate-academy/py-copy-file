def copy_file(cp_command: str) -> None:

    file_list = cp_command.strip().split()
    if len(file_list) != 3:
        return

    if file_list[0] != "cp":
        return

    if file_list[1] == file_list[2]:
        return

    try:
        with (open(file_list[1], "r") as file_in,
              open(file_list[2], "w") as file_out):

            file_out.write(file_in.read())
    except FileNotFoundError:
        return
