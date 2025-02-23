def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "cp":
        return
    _, file_read, new_file = command.split()
    if file_read == new_file:
        return

    try:
        with (open(file_read, "r", encoding="utf-8") as file_in,
              open(new_file, "w", encoding="utf-8") as file_out):
            for line in file_in:
                file_out.write(line)
    except FileNotFoundError:
        return
