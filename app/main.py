def copy_file(command: str) -> None:
    command, old_file, new_file = command.split()
    if old_file == new_file or command != "cp":
        return
    with open(old_file, "r") as file_in, open(new_file, "w") as file_out:
        text = file_in.read()
        file_out.write(text)
