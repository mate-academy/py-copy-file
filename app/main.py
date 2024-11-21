def copy_file(command):
    if command.split(' ')[1] != command.split(' ')[2]:
        with open(command.split(' ')[1], "r") as source:
            with open(command.split(' ')[2], "w") as destination:
                destination.write(source.read())
