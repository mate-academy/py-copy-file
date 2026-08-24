def copy_file(command: str) -> None:
    if not command:
        return
    my_list = command.split(" ")
    if len(my_list) != 3 or my_list[0] != "cp":
        return
    if my_list[1] == my_list[2]:
        return
    try:
        with (open(my_list[1], "r") as
              first_file,
              open(my_list[2], "w") as
              second_file):
            for line in first_file:
                second_file.write(line)
    except FileNotFoundError:
        return
