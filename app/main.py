def copy_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "cp":
        print("Invalid command format.")
        return

    source_filename = parts[1]
    destination_filename = parts[2]

    if source_filename == destination_filename:
        print("Source and destination files are the same. No action taken.")
        return

    try:
        with open(source_filename, "r") as source_file, \
                open(destination_filename, "w") as destination_file:
            content = source_file.read()
            destination_file.write(content)
        print(f"File '{source_filename}' successfully copied to "
              f"'{destination_filename}'.")
    except FileNotFoundError:
        print(f"File '{source_filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
