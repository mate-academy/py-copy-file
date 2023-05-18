def copy_file(command: str) -> None:
    commands = command.split()
    if len(commands) < 3 or len(commands) > 3:
        raise ValueError("Value isn't valid. It should contain "
                         "command 'cp' and names of 2 files")
    if commands[0] == "cp" and (
        commands[1] != commands[2]
    ):
        with (
            open(commands[1], "r") as source_file,
            open(commands[2], "w") as copy_file
        ):
            content = source_file.read()
            copy_file.write(f"{content}")
