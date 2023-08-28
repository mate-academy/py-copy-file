def copy_file(command: str) -> None:
    command, old_file, file_copy = command.split()

    if old_file == file_copy or command != "cp":
        return

    with open(old_file, "r") as file_in, open(file_copy, "w") as file_out:
        content = file_in.read()
        file_out.write(content)
