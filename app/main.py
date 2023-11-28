def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "cp":
        print("Invalid command")
        return
    source, destination = parts[1], parts[2]
    if source == destination:
        return
    with open(source, "r") as file_from, open(destination, "w") as file_to:
        file_to.write(file_from.read())
