def copy_file(command: str) -> None:
    command = command.split()
    if command[0] != "cp" or command[1] == command[2]:
        return
    with open(command[1], "r") as source_file, \
            open(command[2], "w") as file_for_copy:
        for line in source_file:
            file_for_copy.write(line)
