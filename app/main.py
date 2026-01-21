def copy_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "cp":
        return

    _, file1, file2 = parts

    if file1 == file2:
        return

    try:
        with open(file1, "r") as file_in, open(file2, "w") as file_out:
            file_out.write(file_in.read())
    except FileNotFoundError:
        print(f"Error: File '{file1}' not found")
