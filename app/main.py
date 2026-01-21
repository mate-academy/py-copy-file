def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "cp":
        return

    src_file = parts[1]
    dest_file = parts[2]

    if src_file == dest_file:
        return

    try:
        with (open(src_file, "r") as file_in,
              open(dest_file, "w") as file_out):
            content = file_in.read()
            file_out.write(content)
    except FileNotFoundError:
        pass
