def copy_file(command: str):
    file_names = command.split()
    if file_names[1] != file_names[2]:
        with open(file_names[1], "r") as file_old, open(file_names[2], "w") as file_new:
            file_new.write(file_old.read())
