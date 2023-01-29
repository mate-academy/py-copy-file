class CommandError(Exception):
    pass


def copy_file(command: str) -> None:
    command = command.split()
    if len(command) != 3 or command[0] != "cp":
        raise CommandError("Check input command")
    with open(command[1], "r") as input_file, open(command[2], "w") as output_file:
        output_file.write(input_file.read())
