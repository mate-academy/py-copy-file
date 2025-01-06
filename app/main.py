def copy_file(command: str) -> None:
    parts = command.split()
    _, file_in, file_out = parts
    if file_in == file_out:
        return
    with open(file_in, "r") as f_in, open(file_out, "w") as f_out:
        content = f_in.read()
        f_out.write(content)


copy_file("cp file.txt new_file.txt")
