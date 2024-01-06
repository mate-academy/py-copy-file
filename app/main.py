def copy_file(command: str) -> None:
    if len(command.split()) < 3:
        pass

    cp, file1, file2 = command.split()

    if file1 == file2 or not command.startswith(cp):
        pass

    with open(file1, "r") as file_in, open(file2, "w") as file_out:
        content = file_in.read()
        file_out.write(content)
