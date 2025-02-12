def copy_file(command: str) -> None:
    new_file = command.split()
    test1 = new_file[1]
    test2 = new_file[2]
    if not "cp" == new_file:
        return
    elif test1 == test2:
        return
    with open(test1, "r") as file_in, open(test2, "w") as file_out:
        file_out.write(file_in.read())
