def copy_file(command: str) -> None:
    parts = command.strip().split()

    if len(parts) != 3 or parts[0] != "cp":
        print("Invalid command format.")
        return

    _, source, destination = parts

    if source == destination:
        return  # Do nothing if names are the same

    try:
        with open(source, "r", encoding="utf-8") as file_in, \
             open(destination, "w", encoding="utf-8") as file_out:
            file_out.write(file_in.read())
    except FileNotFoundError:
        print(f"Source file '{source}' not found.")
    except IOError as e:
        print(f"Error during file copy: {e}")
