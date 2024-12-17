def copy_file(command: str) -> None:
    split = command.split(" ")
    command = split[0]

    if command != "cp":
        return

    file1 = split[1]
    file2 = split[2]

    if file1 == file2:
        return

    with open(file1, "r") as file_in, open(file2, "w") as file_out:
        file_out.writelines(file_in.readlines())
