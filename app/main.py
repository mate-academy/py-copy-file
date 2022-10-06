def copy_file(command: str) -> str | None:
    command_list = command.split()

    if command_list[0] != "cp":
        return f"unknown command: {command_list[0]}"

    file_to_copy = command_list[1]
    copy_of_file = command_list[2]

    if file_to_copy == copy_of_file:
        return f'file with name "{file_to_copy}" already exists'

    with open(file_to_copy, "r") as file_original, \
            open(copy_of_file, "w") as file_copy:
        file_copy.write(file_original.read())
