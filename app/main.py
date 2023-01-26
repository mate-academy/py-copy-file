def copy_file(command: str):
    old_file_name, new_file_name = command.split()[1:]
    with open(old_file_name, "r") as old_file:
        context = old_file.read()
    with open(new_file_name, "w") as new_file:
        new_file.write(context)
