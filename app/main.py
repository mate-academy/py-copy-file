def copy_file(command: str):
    old_file_name = command.split()[1]
    new_file_name = command.split()[2]
    if old_file_name == new_file_name:
        return 0
    with open(old_file_name, "r") as file:
        content = file.readlines()
    with open(new_file_name, "w") as file:
        file.writelines(content)

# copy_file("cp file.txt new_file.txt")
