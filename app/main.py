def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3:
        print("Invalid command format. Use 'cp source_file destination_file'.")
        return
    
    _, source_file, destination_file = parts
    if source_file == destination_file:
        print("Source and destination files have the same name. Doing nothing.")
        return
    
    try:
        with open(source_file, 'r') as src_file:
            content = src_file.read()
            with open(destination_file, 'w') as dest_file:
                dest_file.write(content)
        print(f"File '{source_file}' copied to '{destination_file}' successfully.")
    except FileNotFoundError as e:
        print(f"Error: {e}")