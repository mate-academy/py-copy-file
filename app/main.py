def copy_file(command: str) -> None:
    command_list = command.split()
    from_file = command_list[1]
    to_file = command_list[2]

    if from_file != to_file:
        with open(from_file, "r") as file_out, open(to_file, "w") as file_in:
            file_in.write(file_out.read())
