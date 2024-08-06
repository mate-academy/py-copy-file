def copy_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "cp":
        raise ValueError("Invalid command format")

    src_file, dest_file = parts[1], parts[2]

    if src_file == dest_file:
        return

    with open(src_file, "r") as file_in, open(dest_file, "w") as file_out:
        file_out.write(file_in.read())
