class LenError(Exception):
    """Raise, when len of list less or more than 3"""


def copy_file(command: str) -> None:
    command = command.split()

    if "cp" not in command:
        print("Unknow command")
        return

    if len(command) != 3:
        raise LenError(f"You enter more or less commands")

    if command[1] == command[2]:
        print("Files name the same")
        return

    with open(command[1], "r") as file_in, open(command[2], "w") as file_out:
        file_out.write(file_in.read())
