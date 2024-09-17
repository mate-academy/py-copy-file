def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "cp":
        raise ValueError
    file1, file2 = parts[1:3]

    if file1 == file2:
        return

    with open(file1, "r") as file_in, open(file2, "w") as file_out:
        file_out.write(file_in.read())
