class InvalidCommandError(Exception):
    ...


def copy_file(command: str) -> None:
    command_list = command.split()
    if command_list[0] != "cp" or len(command_list) != 3:
        raise InvalidCommandError("Unknown command.")
    if command_list[1] != command_list[2]:
        with (
            open(command_list[1], "r") as source_file,
            open(command_list[2], "w") as new_file
        ):
            new_file.write(source_file.read())
