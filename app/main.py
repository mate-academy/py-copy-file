def copy_file(command):
    with open(command.split(' ')[1], "r") as source:
        with open(command.split(' ')[2], "w") as destination:
            if command.split(' ')[1] != command.split(' ')[2]:
                destination.write(source.read())
