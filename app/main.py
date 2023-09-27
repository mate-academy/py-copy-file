def copy_file(command: str) -> None:
    source_file_name, new_file_name = command.split()[1:3]
    with open(source_file_name) as file, open(new_file_name, "w") as new_file:
        new_file.write(file.read())
