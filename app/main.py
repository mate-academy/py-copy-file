def copy_file(command: str) -> None:
    commands_list = command.split()
    copy_command = commands_list[0]
    old_file = commands_list[1]
    new_file = commands_list[2]
    if copy_command != "cp":
        raise NameError(f"{copy_command} is not a valid command.")
    if old_file == new_file:
        raise ValueError(f"File {old_file} and {new_file} have same name")
    with open(old_file, "r") as file_in, open(new_file, "w") as file_out:
        for line in file_in:
            file_out.write(line)
