def copy_file(command: str):
    list_commands = command.split()
    command = list_commands[0]
    first_file = list_commands[1]
    new_file = list_commands[2]

    if first_file == new_file and command != "cp":
        return None

    with open(first_file, "r") as file_in, open(new_file, "w") as file_out:
        file_out.write(file_in.read())
    return "Complete!"
