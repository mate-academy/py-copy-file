def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "cp":
        print("Invalid command format. Use 'cp source_file destination_file'")
        return

    source_file = parts[1]
    destination_file = parts[2]

    if source_file == destination_file:
        print("Source and destination file names are the same."
              "Nothing to copy.")
        return

    try:
        with (open(source_file, "rb") as source,
              open(destination_file, "wb") as destination):
            destination.write(source.read())
        print(f"File '{source_file}' "
              f"copied to '{destination_file}' successfully.")
    except FileNotFoundError:
        print(f"File '{source_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
