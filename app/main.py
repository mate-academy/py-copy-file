def copy_file(command: str) -> None:
    command_name, first_file, second_file, *_ = command.split()

    if first_file == second_file or command_name != "cp":
        return

    with open(first_file, "r") as first, open(second_file, "w") as second:
        second.write(first.read())
