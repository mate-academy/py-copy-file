def copy_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "cp":
        raise ValueError

    original_file = parts[1]
    copy_file = parts[2]

    if original_file == copy_file:
        return

    with open(original_file, "r") as file_in, open(copy_file, "w") as file_out:
        file_out.write(file_in.read())
