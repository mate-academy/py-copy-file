def copy_file(command: str) -> None:

    command = command.split(" ")

    command_name = command[0]
    copied_file = command[1]
    new_file_name = command[2]

    if command_name != "cp" or \
            copied_file == new_file_name or len(command) != 3:
        return

    with open(copied_file, "r") as file_in, \
            open(new_file_name, "w") as file_out:
        file_out.write(file_in.read())
