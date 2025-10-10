import os.path


def copy_file(command: str) -> None:
    splited_command = command.split()

    if len(splited_command) < 3:
        return

    command = splited_command[0]
    in_name = splited_command[1]
    out_name = splited_command[2]

    if command != "cp":
        return

    if not os.path.isfile(in_name):
        return

    if in_name == out_name:
        return

    with open(in_name, "r") as file_in, open(out_name, "w") as file_out:
        content = file_in.read().rstrip("\n")
        file_out.write(content)
