def copy_file(command: str) -> None:
    # Split the command string into its components
    parts = command.split()

    # Check if the command is formatted correctly
    if len(parts) != 3 or parts[0] != "cp":
        print(
            "Invalid command format. Use 'cp source_file destination_file'."
        )
        return

    source_file, dest_file = parts[1], parts[2]

    # Check if the source and destination files are the same
    if source_file == dest_file:
        print(
            "Source and destination file names are the same. Nothing to copy."
        )
        return

    # Perform the file copy
    try:
        with open(source_file, "r") as file_in, \
                open(dest_file, "w") as file_out:
            file_out.write(file_in.read())
        print(f"File '{source_file}' copied to '{dest_file}' successfully.")
    except FileNotFoundError:
        print("One or both files not found. Please check the file names.")
