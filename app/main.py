def copy_file(command: str) -> None:
    cp, source, destination = command.split()
    if cp != "cp" or source == destination:
        return
    with open(source, "r") as file_in, open(destination, "w") as file_out:
        file_out.write(file_in.read())
