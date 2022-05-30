def copy_file(command):
    command = command.split()
    if command[0] == "sp" and command[1] != command[2]:
        with open(command[1], "r") as old_file:
            with open(command[2], "w") as new_file:
                new_file.write(old_file.read())
