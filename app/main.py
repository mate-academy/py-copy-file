def copy_file(comand: str) -> None:
    cmd, file1, file2 = comand.split()
    if not file1 == file2 and cmd == "cp":
        with open(file1, "r") as f1, open(file2, "w") as f2:
            f2.write(f1.read())
