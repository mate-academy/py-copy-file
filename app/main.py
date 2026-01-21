# write your code here
def copy_file(command: str) -> None:
    if len(command) != 0:
        commands = command.split()
        if len(commands) == 3 and commands[0] == "cp":
            if commands[1] != commands[2]:
                try:
                    file_name = commands[1]
                    new_file_name = commands[2]
                    with (open(file_name, "r") as file_in,
                          open(new_file_name, "w") as file_out):
                        for line in file_in:
                            file_out.write(line)
                except FileNotFoundError:
                    pass
