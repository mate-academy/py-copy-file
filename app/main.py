def copy_file(command):
    command = command.split()
    if command[1] == command[2]:
        return
    with open(command[1], "r") as f, open(command[2], "w") as ff:
        ff.write(f.read())
