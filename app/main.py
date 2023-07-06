def copy_file(command: str) -> None:
    elements_of_command = command.split()
    file_to_copy = elements_of_command[1]
    new_file = elements_of_command[2]

    if file_to_copy == new_file:
        return None
    else:
        with (
            open(file_to_copy, "r") as file_in,
            open(new_file, "w") as file_out
        ):
            file_out.write(file_in.read())
