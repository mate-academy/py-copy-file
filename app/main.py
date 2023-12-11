def copy_file(command: str) -> None:
    command = command.split()
    file_source = command[1]
    file_new = command[2]
    if file_source == file_new:
        return
    with open(file_source, "r") as file_in, open(file_new, "w") as file_out:
        file_out.write(file_in.read())
