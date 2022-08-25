def copy_file(command):
    list = command.split()
    if list[1] != list[2]:
        with open(f"{list[1]}", "r") as firstfile, \
                open(f"{list[2]}", "a") as secondfile:
            for line in firstfile:
                secondfile.write(line)
    else:
        pass
