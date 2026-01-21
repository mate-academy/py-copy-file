def copy_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "cp":
        print("Invalid command")
        return

    source_filename, target_filename = parts[1], parts[2]

    if source_filename == target_filename:
        pass

    try:
        with open(source_filename, "r") as source_file:
            content = source_file.read()

        with open(target_filename, "w") as target_file:
            target_file.write(content)

    except FileNotFoundError:
        print(f"Source file {source_filename} not found.")
