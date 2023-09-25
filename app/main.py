class CommandError(Exception):
    """Checks command input for right format."""


def check_command(func: callable) -> callable:
    def wrapper(command: str) -> callable:
        if command.split(" ")[0] != "cp" or len(command.split(" ")) < 3:
            raise CommandError("Please enter valid command")
        return func(command)

    return wrapper


@check_command
def copy_file(command: str) -> None:
    source_name, target_name = command.split(" ")[1:3]
    if source_name == target_name:
        return
    with open(source_name, "r") as source, open(target_name, "w") as target:
        target.write(source.read())
