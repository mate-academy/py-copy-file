def copy_file(command: str) -> None:
    operation, source_file_name, new_file_name = command.split()
    if operation != "cp":
        return
    with open(source_file_name, "r") as source:
        with open(new_file_name, "w") as new_file:
            new_file.writelines(source.read())
