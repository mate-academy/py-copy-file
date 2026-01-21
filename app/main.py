def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "cp":
        print("Invalid command")
        return
    source_file = parts[1]
    destination_file = parts[2]

    if source_file == destination_file:
        print("Source and destination cannot be the same")
        return
    try:
        with (open(source_file, "r") as file_in,
              open(destination_file, "w") as file_out):
            for line in file_in:
                file_out.write(line)
    except FileNotFoundError:
        print(f"Error: Source file '{source_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
