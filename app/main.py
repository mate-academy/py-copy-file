class WrongCommand(Exception):
    pass


class IncorrectCommandFormat(Exception):
    pass


def copy_file(command: str) -> None:
    command_list = command.split()

    if len(command_list) != 3:
        raise IncorrectCommandFormat(
            "Expected format: 'cp source_file_name copy_file_name'"
        )
    if command_list[0] != "cp":
        raise WrongCommand("Command must start with 'cp'")
    if command_list[1] == command_list[2]:
        return

    with (
        open(command_list[1], "r") as file_in,
        open(command_list[2], "w") as file_out
    ):
        file_out.write(file_in.read())
