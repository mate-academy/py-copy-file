def copy_file(command: str) -> None:
    cmd, file_name, copy_file_name = command.split()
    if file_name == copy_file_name or cmd != "cp":
        return
    with open(file_name) as file, open(copy_file_name, "w") as new_file:
        new_file.write(file.read())
