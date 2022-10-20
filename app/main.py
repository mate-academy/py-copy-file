def copy_file(command: str) -> None:
    if len(command.split()) != 3:
        return
    action, old_file, new_file = command.split()
    if action != "cp" or old_file == new_file:
        return
    with open(old_file, "r") as file_in, open(new_file, "w") as file_out:
        file = file_in.read()
        file_out.write(file)
