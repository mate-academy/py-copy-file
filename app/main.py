def copy_file(command: str) -> None:
    command, file_name, new_file_name = command.split()
    if command != "cp":
        return
    file_content = ""
    if file_name == new_file_name:
        return
    with open(file_name, "r") as f:
        file_content = f.read()
    with open(new_file_name, "w") as f:
        f.write(file_content)
