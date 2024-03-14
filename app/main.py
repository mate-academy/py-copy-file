class CommandError(Exception):
    def __str__(self) -> str:
        return "Use: cp <file> <file_copy>"


def copy_file(command: str) -> None:
    if not command:
        raise CommandError

    command = command.split()
    if len(command) != 3 or command[0] != "cp":
        raise CommandError
    if command[1] != command[2]:
        with (
            open(command[1], "r") as file_to_copy,
            open(command[2], "w") as file_to_paste
        ):
            file_to_paste.write(file_to_copy.read())
