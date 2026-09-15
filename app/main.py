def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "cp":
        return

    first_filename = parts[1]
    last_filename = parts[2]

    if first_filename == last_filename:
        return

    try:
        with (open(first_filename, "r") as source_file,
              open(last_filename, "w") as destination_file):
            destination_file.write(source_file.read())
    except FileNotFoundError:
        return
