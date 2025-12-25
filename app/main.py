def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "cp":
        print("Invaild command format")
        return
    _, source, destination = parts
    if source == destination:
        return
    with open(source, "r") as file_in, open(destination, "w") as file_out:
        file_out.write(file_in.read())
