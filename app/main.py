def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "cp":
        raise ValueError
    file1 = parts[1]
    file2 = parts[2]

    if file1 == file2:
        return

    with open(file1, "r") as file_in, open(file2, "w") as file_out:
        file_out.write(file_in.read())
