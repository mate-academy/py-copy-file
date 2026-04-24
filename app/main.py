def copy_file(command: str) -> None:
    # Split the command into parts
    parts = command.split()

    # Check if the command is in the correct format
    if len(parts) != 3 or parts[0].lower() != "cp":
        print("Invalid command format. Use: cp <source> <destination>")
        return

    if parts[1] == parts[2]:
        print("Source and destination files cannot be the same.")
        return

    try:
        with (
            open(parts[1], "rb") as src_file,
            open(parts[2], "wb") as dest_file
        ):
            dest_file.write(src_file.read())

    except Exception as e:
        print(f"An unknown error occurred: {e}")
