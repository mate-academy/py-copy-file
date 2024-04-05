def copy_file(command: str) -> None:
    list_of_names = command.split()
    old_file = list_of_names[0]
    new_file = list_of_names[1]
    if old_file == new_file:
        return
    with open(old_file, "r") as file_in, open(new_file, "w") as file_out:
        content = file_in.read()
        file_out.write(content)
