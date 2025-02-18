def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) < 3 or parts[0] != "cp":
        return

    in_file = parts[1]
    out_file = parts[2]

    if in_file == out_file:
        return

    with open(in_file, "r") as file_in, open(out_file, "w") as file_out:
        file_out.write(file_in.read())
