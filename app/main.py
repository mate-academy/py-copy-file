def copy_file(command: str) -> None:
    cmd_parts = command.strip().split()

    if len(cmd_parts) != 3 or cmd_parts[0] != "cp":
        print("Invalid command format. Use: 'cp source_file destination_file'")
        return

    source, destination = cmd_parts[1], cmd_parts[2]

    if source == destination:
        print("Source and destination are the same. Nothing to copy.")
        return

    try:
        with open(source, "r") as file_in, open(destination, "w") as file_out:
            file_out.write(file_in.read())
        print(f"Copied from '{source}' to '{destination}'.")
    except FileNotFoundError:
        print(f"File '{source}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
