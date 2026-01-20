class CommandError(Exception):
    pass


def copy_file(command: str) -> None:
    command_list = command.split(" ")

    if len(command_list) != 3:
        return

    if (
        command_list[0] == "cp" and
        command_list[1] != command_list[2]
    ):
        with (
            open(command_list[1], "r") as file_in,
            open(command_list[2], "w") as file_out,
        ):
            reader = file_in.read()
            file_out.write(reader)
    else:
        raise CommandError
