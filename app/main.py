def copy_file(command: str) -> None:
    command = command.split()
    file_name1 = command[1]
    file_name2 = command[2]
    if file_name1 == file_name2 and command[0] == "cp":
        return
    with open(file_name1, "r") as file_in, open(file_name2, "w") as file_out:
        for line in file_in.readlines():
            file_out.write(line)
