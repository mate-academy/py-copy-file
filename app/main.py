import os


def copy_file(command: str) -> None:
    commands = command.split()
    if len(commands) != 3 or commands[0] != "cp":
        return
    from_file_name = commands[1]
    if_file_name = commands[2]

    if from_file_name == if_file_name:
        return
    if not os.path.exists(from_file_name):
        return

    with open(from_file_name, "r") as file_in:
        contains = file_in.read()

    with open(if_file_name, "w") as file_out:
        file_out.write(contains)
