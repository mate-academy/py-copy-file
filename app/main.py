def copy_file(command: str) -> None:
    try:
        cp_command, old_file, new_file = command.split()
    except ValueError:
        return
    if old_file != new_file and cp_command == "cp":
        with open(old_file, "r") as first, open(new_file, "w") as second:
            text = first.readline()
            second.write(text)
