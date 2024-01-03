def copy_file(command: str) -> None:
    command_arguments = command.split()

    if len(command_arguments) != 3:
        raise ValueError("Invalid command. The right format is"
                         " 'cp [source_file] [destination_file]'.")

    command, source_file, destination_file = command_arguments

    if command != "cp":
        raise ValueError("Invalid command. Maybe you meant 'cp ...'?")

    if source_file == destination_file:
        raise ValueError("Can't create a new file with the same name.")

    with (open(f"{source_file}", "r") as original_file,
          open(f"{destination_file}", "w") as copied_file):
        copied_file.write(original_file.read())
