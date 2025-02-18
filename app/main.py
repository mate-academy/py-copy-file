def copy_file(command: str) -> None:
    commands = command.split(" ")
    if commands[0] == "cp":
        if commands[1] != commands[2]:
            with open(commands[1], "r") as input_file, \
                    open(commands[2], "w") as output_file:
                file_in = input_file.readlines()
                output_file.writelines(file_in)
