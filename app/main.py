def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "cp":
        return
    part, source_file, destination_file = parts
    if source_file == destination_file:
        return
    try:
        with open(source_file , "r") as file_in:
            content = file_in.read()
        with open(destination_file , "w") as file_out:
            file_out.write(content)
    except FileNotFoundError:
        print("File not found")
