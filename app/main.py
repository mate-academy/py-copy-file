def copy_file(command: str) -> None:
    if len(command.split()) == 3 and command.split[0] == "cp":

        source = command.split()[1]
        destination = command.split()[2]

        if source == destination:
            return

        with open(source, "r") as s, open(destination, "w") as d:
            d.write(s.read())
