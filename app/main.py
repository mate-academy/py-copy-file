def copy_file(copy_command: str) -> None:
    old_name = copy_command.split()[1]
    new_name = copy_command.split()[2]
    if old_name == new_name:
        return
    with open(new_name, "r") as file_in, open(old_name, "w") as file_out:
        for string in file_in:
            file_out.write(string)
