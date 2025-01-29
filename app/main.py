def copy_file(command: str) -> None:
    files = command.split()

    if len(files) != 3 and files[0] != "cp":
        return

    file , new_file = files[1], files[2]

    if file == new_file:
        return

    with open(file, "r") as f1,open(file, "w") as f2:
        f2.write(f1)
