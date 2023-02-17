def copy_file(command: str) -> None:
    try:
        cd, old_file, new_file = command.split()
    except ValueError:
        raise ValueError("Write a command correctly. "
                         "Example: cp file1.txt file2.txt")
    if old_file == new_file:
        return

    with open(old_file, "r") as file_in, open(new_file, "w") as file_out:
        file_out.write(file_in.read())
