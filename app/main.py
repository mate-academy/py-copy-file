def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "cp":
        return

    source = parts[1]
    destination = parts[2]

    if source == destination:
        return

    with open(source, "r") as file_in, open(destination, "w") as file_out:
        content = file_in.read()
        file_out.write(content)
