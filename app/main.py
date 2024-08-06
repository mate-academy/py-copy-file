class IncorrectCommand(Exception):
    pass


def copy_file(command: str) -> None:
    command = command.split(" ")
    if len(command) != 3 or "cp" not in command:
        raise IncorrectCommand("Incorrectly written command")
    if command[1] == command[2]:
        return

    with open(command[1], "r") as file_in, open(command[2], "w") as file_out:
        file_out.write(file_in.read())
