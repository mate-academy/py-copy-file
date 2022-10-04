def copy_file(command: str) -> None:
    command_name, file, new_file = command.split()

    if command_name != "cp" or file == new_file:
        return

    with open(file, "r") as main, open(new_file, "w") as copy:
        copy.write(main.read())
