def copy_file(command: str) -> None:
    commands = command.split()
    if len(commands) != 3:
        raise ValueError("command should have 3 arguments")
    if commands[0] != "cp":
        raise ValueError("The command should be 'cp'")
    if commands[1] != commands[2]:
        with (open(commands[1], "r") as first_file,
              open(commands[2], "w") as second_file
              ):
            first_content = str(first_file.read())
            second_file.write(first_content)
