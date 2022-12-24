class CommandNotFound(Exception):
    pass


def copy_file(command: str) -> None:
    elements_of_command = command.split()
    try:
        if elements_of_command[0] != "cp":
            raise CommandNotFound
    except CommandNotFound("You must enter a valid command"):
        raise

    with open(elements_of_command[1], "r") as file_in, \
            open(elements_of_command[2], "w") as file_out:
        if elements_of_command[1] == elements_of_command[2]:
            return
        file_out.write(file_in.read())
