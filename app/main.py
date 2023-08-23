def copy_file(command: str) -> str:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "cp":
        return "Invalid command. Please provide a valid 'cp' command."

    if parts[1] == parts[2]:
        return

    with open(parts[1], "r") as file1, open(parts[2], "w") as file2:
        new_file = file1.read()
        file2.write(new_file)
