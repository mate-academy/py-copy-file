def copy_file(command: str) -> None:
    words = command.split()
    file1 = words[1]
    file2 = words[2]

    if file1 == file2:
        return None

    with open(file1, "r") as f_in, open(file2, "w") as f_out:
        f_out.write(f_in.read())
