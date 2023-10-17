def copy_file(command: str) -> None:
    cp_command = command.split()
    if validate_cp_command(cp_command):
        with (open(cp_command[1], "r") as file,
              open(cp_command[2], "w") as new_file):
            content = file.read()
            new_file.write(content)


def validate_cp_command(cp_command: list) -> bool:
    if cp_command[0] != "cp":
        return False
    if cp_command[1] == cp_command[2]:
        return False
    return True
