def copy_file(command: str):
    list_of_commands = command.split()
    start = list_of_commands[1]
    end = list_of_commands[2]

    if start != end:
        with open(start, "r") as start_f:
            with open(end, "w") as end_f:
                end_f.write(start_f.read())
