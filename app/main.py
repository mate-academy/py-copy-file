def copy_file(command: str) -> None:
    command = command.split()
    copied_data = None
    with open(command[1], "r") as file_to_copy:
        copied_data = file_to_copy.read()
    with open(command[2], "w") as new_file:
        new_file.write(copied_data)
