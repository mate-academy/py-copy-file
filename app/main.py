def copy_file(command):
    old_file = command.split()[1]
    new_file = command.split()[2]

    if old_file != new_file:
        with open(old_file, "r") as source:
            with open(new_file, "w") as destination:
                destination.write(source.read())
