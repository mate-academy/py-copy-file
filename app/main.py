def copy_file(command: str) -> None:
    result = command.split()
    if result[1] == result[2]:
        print("Same file")
    else:
        with open(result[1], "r") as fin, open(result[2], "w+") as fout:
            fout.write(fin.read())

    copy_file("cp file.txt file2.txt")
