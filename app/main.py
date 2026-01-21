def copy_file(command):
    stre = command.split(" ")
    if len(stre) != 3:
        return
    if stre[0] != "cp":
        return
    _, source, destination = stre
    if source == destination:
        return
    else:
        try:
            with open(source, "r") as file_in, open(destination, "w") as file_out:
                content = file_in.read()
                file_out.write(content)
        except FileNotFoundError:
            return


