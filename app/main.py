def copy_file(command: str):
    cp, file1, file2 = command.split()
    if file1 != file2:
        with open(file1, "r") as f1:
            with open(file2, "w") as f2:
                f2.write(f1.read())
