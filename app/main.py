import shutil


def copy_file(command: str) -> None:
    command = command.split(" ")
    if len(command) == 3 and command[0] == "cp":
        shutil.copy(command[1], command[2])
        return
    print("Invalid command")
    return
