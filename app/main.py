class UnknownCommand(Exception):
    pass


def copy_file(command: str) -> None:
    cmd = command.split(" ")
    if cmd[0] == "cp":
        if cmd[1] != cmd[2]:
            try:
                with open(cmd[1], "r") as source, open(cmd[2], "w") as target:
                    lines = source.readlines()
                    for line in lines:
                        target.write(line)
            except FileNotFoundError:
                print(f"File {cmd[1]} does not exist!")
            except IOError:
                print("An error occurred while processing the files.")
    else:
        raise UnknownCommand("Use format: 'cp source_file destination_file'.")
