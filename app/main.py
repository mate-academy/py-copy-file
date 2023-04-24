

def copy_file(command: str) -> None:
    names = command.split()
    if names[1] == names[2] or\
            len(command.split()) != 3 or\
            command.split()[0] != "cp":
        return
    with open(names[1], "r") as f_r, open(names[2], "w") as f_w:
        arr_data = f_r.readlines()
        arr_data_checked = []
        for i in arr_data:
            arr_data_checked.append(i.strip("\n"))
        for line in arr_data_checked:
            f_w.write(line + "\n")


copy_file("cp test1.txt file8.txt")
