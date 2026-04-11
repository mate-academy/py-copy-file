def copy_file(command_line: str) -> None:
    commands = command_line.split(" ")
    if commands[0] == "cp" and len(commands) == 3:
        try:
            with (
                open(commands[1]) as source,
                open(commands[2], "w") as target
            ) :
                target.write(source.read())
        except FileNotFoundError as e:
            print(e)
    else:
        print("Invalid command")
