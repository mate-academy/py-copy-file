def copy_file(command: str):
    parts = command.split()
    if len(parts) != 3 or parts[0] != "cp":
        raise ValueError("Invalid command. Use format: cp source_file target_file")
    source_file, target_file = parts[1], parts[2]
    if source_file == target_file:
        return

    try:
        with open(source_file, "r") as file_in, open(target_file, "w") as file_out:
            file_out.write(file_in.read())
    except FileNotFoundError:
        print(f"Error: File '{source_file}' does not exist")
    except Exception as e:
        print(f"An error occurred: {e}")
