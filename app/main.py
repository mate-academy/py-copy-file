class CommandNotFound(Exception):
    pass


class IncorrectCommand(Exception):
    pass


def copy_file(command: str) -> None:
    command_list = command.split()

    if len(command_list) != 3:
        raise IncorrectCommand("Incorrect command")
    if command_list[0] != "cp":
        raise CommandNotFound("Command 'cp' not found")
    if command_list[1] == command_list[2]:
        return

    with (
        open(command_list[1], "r") as file_in,
        open(command_list[2], "w") as file_out
    ):
        file_out.write(file_in.read())
