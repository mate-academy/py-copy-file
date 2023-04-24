

def copy_file(command: str) -> None:
    names = command.split()
    if names[1] == names[2] or\
            len(command.split()) != 3 or\
            command.split()[0] != "cp":
        return
    with open(names[1], "r") as file_read, open(names[2], "w") as file_write:
        arr_data = file_read.readlines()
        for line in arr_data:
            file_write.write(line + "\n")
