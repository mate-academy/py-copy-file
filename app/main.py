def copy_file(command: str):
    operator, file_name, new_file_name = command.split()

    if file_name != new_file_name and operator == "cp":
        with open(file_name) as file:
            with open(new_file_name, "w") as new_file:
                new_file.write(file.read())
