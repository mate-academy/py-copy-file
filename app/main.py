def copy_file(command: str) -> None:
    if not command.startswith("cp"):
        return
    command = command.split()[1:]
    if len(command) != 2:
        return
    file_source, file_new = command
    if file_source == file_new:
        return
    with open(file_source, "r") as file_in, open(file_new, "w") as file_out:
        file_out.write(file_in.read())
