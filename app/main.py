def copy_file(command: str) -> None:
    parts = command.split(" ")

    if len(parts) != 3 or parts[0] != "cp" or parts[1] == parts[2]:
        raise ValueError("Invalid command format")

    try:
        with open(parts[1], "r") as file, open(parts[2], "w") as copy:
            copy.write(file.read())
    except FileNotFoundError:
        print(f"File: {parts[1]} not found.")
