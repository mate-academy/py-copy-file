def copy_file(command: str) -> None:
    try:
        cmd, file1, file2 = command.split()
    except ValueError:
        print("Command must have 2 arguments")
        return
    if file1 == file2 or cmd != "cp":
        return

    with open(file1, "r") as source, open(file2, "w") as target:
        target.write(source.read())
