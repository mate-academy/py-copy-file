def copy_file(command: str) -> None:
    new_list = command.split()
    if len(new_list) != 3:
        return
    if new_list[1] == new_list[2]:
        return
    if new_list[0] != "cp":
        return
    try:
        with open(new_list[1], "r") as file1, open(new_list[2], "w") as file2:
            file2.write(file1.read())
    except Exception:
        pass
