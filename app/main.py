def copy_file(command: str) -> None:
    command_arguments = command.split()

    if len(command_arguments) != 3:
        raise ValueError("Invalid command. The right format is 'cp [original_file] [copied_file]'.")
    if command_arguments[0] != "cp":
        raise ValueError("Invalid command. Maybe you meant 'cp...'?")
    if command_arguments[1] == command_arguments[2]:
        raise ValueError("Can't create a new file with the same name.")

    with (open(f"{command_arguments[1]}", "r") as original_file,
          open(f"{command_arguments[2]}", "w") as copied_file):
        copied_file.write(original_file.read())
