import os.path


def copy_file(command: str) -> None:
    commands = command.split()
    if len(commands) != 3 or commands[0] != "cp":
        return
    first_file = commands[1]
    second_file = commands[2]
    if first_file == second_file:
        return
    if not os.path.exists(first_file):
        return
    with open(first_file, "r") as f_in, open(second_file, "w") as f_out:
        f_out.write(f_in.read())
