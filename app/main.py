def copy_file(command: str) -> None:
    command_list = command.split()
    existing_file = command_list[1]
    new_file = command_list[2]
    with open(existing_file, "r") as file_in, open(new_file, "w") as file_out:

        if existing_file == new_file:
            return

        for line in file_in:
            file_out.write(line)
