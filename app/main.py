def copy_file(command: str):
    file_name, new_file_name = command.split()[1], command.split()[2]

    if file_name != new_file_name:
        with open(file_name, "r") as file:
            with open(new_file_name, "w") as new_file:
                new_file.write(file.read())
