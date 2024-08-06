def copy_file(command: str) -> str:
    command_parts = command.split()

    if len(command_parts) != 3:
        return "Invalid command format"

    cp_command, source_path, destination_path = command_parts

    if cp_command != "cp":
        return "Invalid command. Must start with 'cp'."

    if source_path == destination_path:
        return "Source and destination paths are the same."

    try:
        with (
            open(source_path, "r") as file_in,
            open(destination_path, "w") as file_out
        ):
            file_out.write(file_in.read())
        return "File copied successfully"
    except FileNotFoundError:
        return f"The file '{source_path}' does not exist."
    except Exception as e:
        return f"An error occurred: {e}"
