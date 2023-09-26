def copy_file(command: str) -> None:
    source_file_name = command.split()[1]
    new_file_name = command.split()[2]
    with open(source_file_name) as file, open(new_file_name, "w") as new_file:
        new_file.write(file.read())
