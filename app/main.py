def copy_file(command: str) -> None:
    command_split = command.split()
    if len(command_split) != 3:
        return

    command_name, from_file, to_file = command_split

    if command_name != "cp" or from_file == to_file:
        return

    with open(from_file, "r") as file_in, open(to_file, "w") as file_out:
        for line in file_in:
            file_out.write(line)
