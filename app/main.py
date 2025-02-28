def copy_file(command: str) -> None:
    command_parts = command.split()

    if len(command_parts) != 3:
        print("Invalid command format. Expected format: 'cp <source_file> <destination_file>'")
        return

    operation, source_file, destination_file = command_parts

    if operation != "cp":
        print("Invalid operation. Use 'cp' to copy files.")
        return

    if source_file == destination_file:
        print("Source and destination files must be different.")
        return

    try:
        with open(source_file, "r") as file_in, open(destination_file, "w") as file_out:
            file_out.write(file_in.read())
            print(f"File '{source_file}' successfully copied to '{destination_file}'!")
    except FileNotFoundError:
        print(f"File '{source_file}' not found.")
