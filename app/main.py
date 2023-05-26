def copy_file(command: str) -> None:
    cmd, file1, file2, args = command.split(maxsplit=3)
    if file1 == file2:
        return

    with open(file1, "r") as source, open(file2, "w") as target:
        target.write(source.read())
