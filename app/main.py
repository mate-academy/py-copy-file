def copy_file(command: str) -> None:
    if len(command.split()) != 3:
        return
    cp, source, destination = command.split()
    if source == destination or cp != "cp":
        return
    with open(source, "r") as file_in, open(destination, "w") as file_out:
        file_out.write(file_in.read())
