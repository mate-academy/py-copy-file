def copy_file(command: str):
    new_command = command.split()
    file = new_command[1]
    new_file = new_command[2]

    if file != new_file:
        with open(file, "r") as origin:
            with open(new_file, "w") as copy:
                copy.write(str(origin.read()))