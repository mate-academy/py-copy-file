def copy_file(cp: str) -> None:
    without_cp = cp.split()
    file_1 = without_cp[1]
    file_2 = without_cp[2]
    if file_1 == file_2:
        return
    with open(file_1, "r") as file1:
        with open(file_2, "w") as file2:
            for line in file1:
                file2.write(line)
