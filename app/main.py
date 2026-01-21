def copy_file(command: str) -> None:
    parts = command.strip().split()
    if len(parts) != 3 or parts[0] != "cp":
        return
    source_name = parts[1]
    destination_name = parts[2]
    if source_name == destination_name:
        return
    try:
        with open(source_name, "r") as f, open(destination_name, "w") as s:
            data = f.read()
            s.write(data)

    except FileNotFoundError:
        return
