def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "cp":
        return
    if parts[1] == parts[2]:
        return
    try:
        with open(parts[1], "r") as file_in, open(parts[2], "w") as file_out:
            read = file_in.read()
            file_out.write(read)
    except FileNotFoundError:
        print(f"File {parts[1]} not found")
