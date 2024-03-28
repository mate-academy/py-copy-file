def copy_file(command: str) -> None:
    files = command.split()
    if files[1] == files[-1]:
        return
    with open(files[1], "r") as copied_file, open(files[-1], "w") as new_file:
        new_file.write(copied_file.read())
