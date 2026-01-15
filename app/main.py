def copy_file(command: str) -> None:

    parts = command.strip().split()
    if len(parts) != 3:
        return

    command_token, source_file_name, destination_file_name = parts
    if command_token != "cp" or source_file_name == destination_file_name:
        return

    try:
        with open(source_file_name, "rb") as source_file, \
             open(destination_file_name, "wb") as destination_file:
            while True:
                chunk = source_file.read(1024 * 1024)  # 1 MB chunks
                if not chunk:
                    break
                destination_file.write(chunk)
    except FileNotFoundError:
        return
