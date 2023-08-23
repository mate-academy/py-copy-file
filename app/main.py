def copy_file(command: str) -> None:
    try:
        key, file_name, copy_name = command.split()
    except IndexError:
        return

    if file_name == copy_name or key != "cp":
        return

    with open(file_name, "r") as old_file, open(copy_name, "w") as file_copy:
        file_content = old_file.read()
        file_copy.write(file_content)
