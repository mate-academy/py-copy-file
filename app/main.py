def copy_file(command: str) -> None:
    command_split = command.split()
    old_file = command_split[1]
    new_file = command_split[2]
    if len(command_split) != 3 or command_split[0] != "cp":
        return
    if old_file == new_file:
        return
    with open(old_file, "r") as file_in, open(new_file, "w") as file_out:
        file_out.write(file_in.read())
