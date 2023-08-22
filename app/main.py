def copy_file(command: str) -> None:
    list_from_command = command.split()
    if len(list_from_command) != 3:
        return
    command, original_file, copy_of_file = command.split()
    if command != "cp":
        return
    if original_file == copy_of_file:
        return
    with open(original_file, "r") as file_in, open(
        copy_of_file, "w"
    ) as file_out:
        file_out.write(file_in.read())
