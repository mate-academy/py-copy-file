def copy_file(file_info: str) -> None:
    if not file_info:
        return
    my_list = file_info.split(" ")
    if len(my_list) < 3 or my_list[0] != "cp":
        return
    if my_list[1] == my_list[2]:
        return
    try:
        with (open(my_list[1], "r") as
              first_file,
              open(my_list[2], "a") as
              second_file):
            for line in first_file:
                second_file.write(line)
    except FileNotFoundError:
        return
