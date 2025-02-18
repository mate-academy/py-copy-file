def copy_file(command: str) -> None:
    if not command.startswith("cp"):
        return
    file_name, copy_name = command.split()[1:]
    if file_name == copy_name:
        return
    with open(file_name, "r") as file, open(copy_name, "w") as copy:
        copy.write(file.read())
