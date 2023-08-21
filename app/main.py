def copy_file(command: str) -> None:
    keys = command.split(" ")
    try:
        file_name = keys[1]
        copy_name = keys[2]
    except IndexError:
        return

    if file_name == copy_name:
        return

    with open(file_name, "r") as old_file, open(copy_name, "w") as file_copy:
        file_content = old_file.read()
        file_copy.write(file_content)
