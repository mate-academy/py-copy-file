def copy_file(command: str) -> None:
    command_parts = command.split()
    name_to_copy = command_parts[1]
    new_file = command_parts[2]
    if name_to_copy == new_file:
        return
    with open(name_to_copy, "r") as file_in, open(new_file, "w") as file_out:
        data = file_in.read()
        file_out.write(data)
