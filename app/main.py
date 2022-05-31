def copy_file(command: str):
    cmdList = command.split()
    if cmdList[1] == cmdList[2]:
        print("Same file")
    else:
        with open(cmdList[1], "r") as fin, open(cmdList[2], "w+") as fout:
            fout.write(fin.read())


copy_file("cp file.txt file2.txt")
