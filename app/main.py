def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "cp":
        print("Invalid command format. Usage: cp source_file target_file")
        return

    source, destination = parts[1], parts[2]

    # Do nothing if the source and destination are the same
    if source == destination:
        return

    try:
        with open(source, "r") as file_in, open(destination, "w") as file_out:
            file_out.write(file_in.read())
    except FileNotFoundError:
        print(f"File not found: {source}")
    except Exception as e:
        print(f"An error occurred: {e}")
