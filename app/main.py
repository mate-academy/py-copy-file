def copy_file(command):
    ls = command.split()
    if ls[1] != ls[2]:
        with open(f"{ls[1]}", "w") as f:
            f.write("something")
        with open(f"{ls[1]}", "r") as f1:
            content = f1.read()
            with open(ls[2], "w") as f2:
                f2.write(content)


copy_file("cp file.txt new_file.txt")
