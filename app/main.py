def copy_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "cp":
        return

    source = parts[1]
    destination = parts[2]

    if source == destination:
        return

    try:
        with (open(source, "r") as source_file,
              open(destination, "w") as destination_file):
            content = source_file.read()
            destination_file.write(content)
    except FileNotFoundError:
        print("nie znaleziono pliku")
