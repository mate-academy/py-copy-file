def copy_file(command: str) -> None:
    if len(command.split()) == 3 and command.split()[0] == "cp":
        filename1 = command.split()[1]
        filename2 = command.split()[2]
    else:
        return

    if filename1 == filename2:
        return

    try:
        with open(filename1, "r") as file1, open(filename2, "a") as file2:
            file2.write(file1.read())
    except FileNotFoundError:
        return
