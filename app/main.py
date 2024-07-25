def copy_file(command: str) -> None:
    commands = command.split(" ")
    if commands[1] != commands[2]:
        with (open(commands[1], "r") as file_for_read,
              open(commands[2], "w") as file_for_write):
            file_for_write.write(file_for_read.read())
