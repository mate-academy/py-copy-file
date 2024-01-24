def copy_file(command: str) -> None:
    components = command.split()
    old_file = components[1]
    file_copy = components[2]
    if old_file == file_copy:
        return

    with open(old_file, "r") as file_in, open(file_copy, "w") as file_out:
        file_out.write(file_in.read())
        return
