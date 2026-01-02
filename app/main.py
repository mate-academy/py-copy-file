def copy_file(command: str) -> None:
    parts = command.strip().split()

    if len(parts) != 3 or parts[0] != "cp":
        print("Invalid command format. Use: cp <source> <destination>")
        return

    source, destination = parts[1], parts[2]

    if source == destination:
        print(f"Source and destination file names are the same: '{source}'. Nothing to do.")
        return

    try:
        with open(source, "r") as file_in, open(destination, "w") as file_out:
            file_out.write(file_in.read())
        print(f"File '{source}' successfully copied to '{destination}'.")
    except FileNotFoundError:
        print(f"Error: Source file '{source}' not found.")
    except PermissionError:
        print(f"Error: Permission denied while accessing '{source}' or '{destination}'.")
    except Exception as e:
        print(f"Unexpected error: {e}")
