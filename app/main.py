def copy_file(command: str):
    command = command.split()
    cmd = command[0]
    old_file = command[1]
    new_file = command[2]

    if old_file == new_file or cmd != "cp":
        return print("Something wrong!")

    with open(old_file, "r") as source_file, \
            open(new_file, "w") as destination_file:
        destination_file.write(source_file.read())
