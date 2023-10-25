def copy_file(command: str) -> None:
    old_file = command.split()[1]
    new_file = command.split()[2]
    if command.split()[0] != "cp" or old_file == new_file:
        return

    with open(old_file, "r") as file_in, open(new_file, "w") as file_out:
        old_file_text = file_in.read()
        file_out.write(old_file_text)
