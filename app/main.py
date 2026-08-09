def copy_file(info: str) -> None:
    list_info = info.split()
    if (len(list_info) < 3
            or list_info[0] != "cp"
            or list_info[1] == list_info[2]):
        return
    try:
        with (open(list_info[1], "r") as file_in,
              open(list_info[2], "w") as file_out):
            file_out.write(file_in.read())
    except FileNotFoundError:
        return
