def copy_file(command: str) -> None:

    commands = command.split()
    if len(commands) == 3 and commands[0] == "cp":
        source_file = commands[1]
        destination_file = commands[2]

        if source_file != copy_file:
            with (open(source_file, "r") as first_file,
                  open(destination_file , "w") as second_file):
                content = first_file.read()
                second_file.write(content)
