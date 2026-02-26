def copy_file(command: str) -> None:
    parts_command = command.split()

    if len(parts_command) != 3:
        print("Invalid command format. Use: cp <source> <destination>")
        return

    cp, source, destination = parts_command

    if cp != "cp":
        print("Invalid command. Command should start with 'cp'.")
        return

    if source == destination:
        print("Source and destination cannot be the same.")
        return
    try:
        with open(source, "r") as src_file:
            content = src_file.read()

    except FileNotFoundError:
        print(f"Source file '{source}' not found.")
        return

    with open(destination, "w") as dest_file:
        dest_file.write(content)
