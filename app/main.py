def copy_file(command: str) -> None:
    command, source, destination = command.split()

    if not (command != "cp" or source == destination):

        with open(source) as source, open(destination, "w") as copy:
            copy.write(source.read())
