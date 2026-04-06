def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "cp":
        return
    file1, file2 = parts[1], parts[2]
    if file1 == file2:
        return

    try:
        with open(file1, "r") as file_in, open(file2, "w") as file_out:
            content = file_in.read()
            file_out.write(content)
    except FileNotFoundError:
        return
