def copy_file(command: str) -> None:
    commands = command.split()

    if commands[0] != commands[1]:
        with (open(commands[0], "r") as file_in,
              open(commands[1], "w") as file_out):
            file_out.writelines(file_in.readlines())
