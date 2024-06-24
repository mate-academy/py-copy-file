def copy_file(command: str) -> None:
    parts = command.split(" ")
    if parts[1] == parts[2]:
        return
    if len(parts) != 3 or parts[0] != "cp":
        raise ValueError("Command must be in the format: cp file_from file_to")
    with open(parts[1], "r") as file_from, open(parts[2], "r") as file_to:
        file_to.write(file_from.read())
