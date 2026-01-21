import os


def copy_file(command: str) -> None:
    command_parts = command.split()

    if len(command_parts) != 3 or command_parts[0] != "cp":
        print("Error: Invalid command. Use format: cp <source> <destination>")
        return

    source_file_path = command_parts[1]
    destination_file_path = command_parts[2]

    if source_file_path == destination_file_path:
        print("Error: Source and destination files cannot be the same.")
        return

    if not os.path.exists(source_file_path):
        print(f"Error: '{source_file_path}' does not exist.")
        return

    with (open(source_file_path, "r") as source_file,
          open(destination_file_path, "w") as destination_file):
        content = source_file.read()
        destination_file.write(content)
