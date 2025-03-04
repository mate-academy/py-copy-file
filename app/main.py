def copy_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "cp":
        return

    file_to_copy = parts[1]
    new_file = parts[2]

    if file_to_copy == new_file:
        return

    try:
        with (open(file_to_copy, "r") as file_in,
              open(new_file, "w") as file_out):
            file_out.write(file_in.read())
    except FileNotFoundError:
        return
