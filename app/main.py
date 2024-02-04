def copy_file(command: str) -> None:
    command_list = command.split()
    if len(command_list) != 3:
        raise ValueError(f"Command must have 3 elements, but got: "
                         f"{len(command_list)}")
    copy_command, old_file, new_file = command_list
    if copy_command != "cp":
        raise NameError(f"{copy_command} is not a valid command.")
    if old_file == new_file:
        raise ValueError(f"File {old_file} and {new_file} have same name")
    try:
        with open(old_file, "r") as file_in, open(new_file, "w") as file_out:
            file_out.write(file_in.read())
    except FileNotFoundError:
        raise ValueError(f"File {old_file} not found.")
