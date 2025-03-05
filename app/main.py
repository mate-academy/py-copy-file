def copy_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "cp":
        return

    source, destination = parts[1], parts[2]

    if source == destination:
        return

    try:
        with (open(source, "r", encoding="utf-8") as file_in,
              open(destination, "w", encoding="utf-8") as file_out):
            file_out.write(file_in.read())
    except FileNotFoundError:
        return
