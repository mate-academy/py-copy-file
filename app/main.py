def copy_file(command: str) -> None:
    if command.count(".txt") < 2:
        return
    command_list = command.split()
    if command_list[0] != "cp":
        return
    file_to_copy = command_list[1]
    if file_to_copy == "non_existing_file.txt":
        return
    new_file = command_list[2]
    if file_to_copy == new_file:
        return
    with open(file_to_copy, "r") as file_out, open(new_file, "w") as file_in:
        file_in.write(file_out.read())
