def copy_file(command: str) -> None:
    parts = command.strip().split()
    if len(parts) != 3 or parts[0] != "cp":
        return
    source = parts[1]
    new_file_name = parts[2]
    if source == new_file_name:
        return
    try:
        with (open(source, "r") as file_in,
              open(new_file_name, "w") as file_out):
            file_out.write(file_in.read())
    except FileNotFoundError:
        return
