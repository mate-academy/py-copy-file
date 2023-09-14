def copy_file(comand: str) -> None:
    file1, file2 = comand.split()[1], comand.split()[2]
    if not file1 == file2:
        with open(file1, "r") as f1, open(file2, "w") as f2:
            f2.write(f1.read())
