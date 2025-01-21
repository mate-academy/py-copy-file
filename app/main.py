def copy_file(command: str) -> None:
    _, old_file, new_file = command.split(" ")
    if old_file == new_file:
        return
    with open(old_file, "r") as file_in, open(new_file, "a") as file_out:
        for line in file_in:
            file_out.write(line)
