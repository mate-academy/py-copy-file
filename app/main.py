class CommandNotFound(Exception):
    pass


def copy_file(command: str) -> None:
    elements_of_command = command.split()
    if elements_of_command[0] != "cp":
        raise CommandNotFound("You must enter a valid command")

    with open(elements_of_command[1], "r") as file_in, \
            open(elements_of_command[2], "w") as file_out:
        if elements_of_command[1] == elements_of_command[2]:
            return
        file_out.write(file_in.read())
