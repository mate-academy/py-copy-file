def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "cp":
        print("Error: Command must be in the format "
              "'cp source_file destination_file'.")
        return

    source_file = parts[1]
    dest_file = parts[2]

    if source_file == dest_file:
        print("Error: Source and destination files are the same. "
              "Copy not performed.")
        return

    try:
        with open(source_file, "r") as file_in:
            content = file_in.read()
        with open(dest_file, "w") as file_out:
            file_out.write(content)
        print(f"File '{source_file}' successfully copied to '{dest_file}'.")
    except FileNotFoundError:
        print(f"Error: File '{source_file}' not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
