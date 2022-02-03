def copy_file(command):
    ls = command.split()
    if ls[0] == "cp" and ls[1] != ls[2]:
        with open(f"{ls[1]}", "r") as fin:
            with open(ls[2], "w") as fout:
                for line in fin:
                    fout.write(line)


copy_file("cp file.txt new_file.txt")
