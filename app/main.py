class CommandError(Exception):
    pass


def copy_file(command: str) -> None:
    command_list = command.split(" ")

    if command_list[0] == "cp":
        with (
            open(command_list[1], "r") as file_in,
            open(command_list[2], "w") as file_out,
        ):
            reader = file_in.read()
            file_out.write(reader)
    raise CommandError
