def copy_file(command: str):
    commands = command.split()
    file, new_file = commands[1], commands[2]

    if file == new_file:
        return

    with open(file, "r") as file_in, open(new_file, "w") as file_out:
        file_out.write(file_in.read())
