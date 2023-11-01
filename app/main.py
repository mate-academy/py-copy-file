def copy_file(command: str) -> None:
    file1, file2 = command.split()[1:]
    if file1 != file2:
        with open(file1, "r") as source, open(file2, "w") as destination:
            destination.write(source.read())
