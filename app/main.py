def copy_file(command: str) -> None:

    command, file_name, copy_name = command.split()

    if file_name == copy_name:
        return

    with open(copy_name, "w") as copy, open(file_name, "r") as file:
        copy.writelines(file.readlines())
