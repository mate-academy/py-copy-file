def copy_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "cp":
        return

    original_file = parts[1]
    copy_name = parts[2]

    if original_file == copy_name:
        return

    try:
        with (open(original_file, "r") as file_in,
              open(copy_name, "w") as file_out):
            file_out.write(file_in.read())
    except FileNotFoundError:
        pass
