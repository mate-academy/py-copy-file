def copy_file(command: str) -> None:
    parts = command.split()
    _, old_file, new_file = parts
    with open(old_file, "r") as file_in, open(new_file, "w") as file_out:
        file_out.write(file_in.read())
