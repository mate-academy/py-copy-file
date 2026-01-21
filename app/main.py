def copy_file(command: str) -> None:
    command = command.split(" ")
    if len(command) == 3:
        try:
            if command[0] == "cp" and command[1] != command[2]:
                with open(command[1], "r") as old_file, \
                        open(command[2], "w") as new_file:
                    for line in old_file:
                        new_file.write(line)
        except (FileNotFoundError):
            pass
