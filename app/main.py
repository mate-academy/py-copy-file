def copy_file(command):
    parts = command.split()
    if parts[0] == 'cp' and len(parts) == 3:
        source_file, dest_file = parts[1], parts[2]
        if source_file == dest_file:
            return
        try:
            with open(source_file, 'r') as file_in, open(dest_file, 'w') as file_out:
                file_out.write(file_in.read())
        except FileNotFoundError:
            print(f"File {source_file} not found.")
