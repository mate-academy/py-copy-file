def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) == 3:
        command, file1, file2 = parts
        if file1 != file2 and command == "cp":
            with open(file1, "r") as source, open(file2, "w") as destination:
                destination.write(source.read())
