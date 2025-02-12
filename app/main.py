def copy_file(command: str) -> None:
    new_file = command.split()
    test1 = new_file[1]
    test2 = new_file[2]

    if len(new_file) != 3 or "cp" != new_file[0] or test1 == test2:
        return
    with open(test1, "r") as file_in, open(test2, "w") as file_out:
        file_out.write(file_in.read())
