def copy_file(command: str) -> None:
    cmd, file1, file2 = command.split()
    if cmd == "cp" and file1 != file2:
        with open(file1, "r") as file_in, open(file2, "w") as file_out:
            text = file_in.read()
            file_out.write(text)
