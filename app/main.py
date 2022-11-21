def copy_file(command: str) -> None:
    splited_command = command.split()

    if splited_command[0] == "cp" and splited_command[1] != splited_command[2]:
        with open(splited_command[1], "r") as \
                old_file, open(splited_command[2], "w") as new_file:
            read_file = old_file.read()
            new_file.write(read_file)

    elif command[1] == command[2]:
        raise Exception("Names are equal!")
