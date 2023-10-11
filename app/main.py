def copy_file(command: str) -> None:
    cmd = command.split()[0]
    source = command.split()[1]
    destination = command.split()[2]
    if source != destination and cmd == "cp":
        with open(source, "r") as file_in, open(destination, "w") as file_out:
            file_out.write(file_in.read())
