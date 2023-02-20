def copy_file(command: str) -> None:
    commands = command.split()
    old_file = commands[1]
    new_file = commands[2]
    if old_file == new_file:
        return
    with open(old_file, "r") as source:
        content = source.read()

    with open(new_file, "w") as destination:
        destination.write(content)
