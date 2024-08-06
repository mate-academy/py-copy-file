def copy_file(command: str) -> None:
    command_parts = command.split()
    if len(command_parts) != 3 or command_parts[0] != "cp":
        print("Invalid command format")
        return

    cp_command, source_path, destination_path = command_parts

    if source_path == destination_path:
        print("Source and destination paths are the same.")
        return

    try:
        with (
            open(source_path, "r") as file_in,
            open(destination_path, "w") as file_out
        ):
            file_out.write(file_in.read())
    except FileNotFoundError:
        print(f"The file '{source_path}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")
