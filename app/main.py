def copy_file(command: str) -> None:
    command, olf_file, new_file = command.split()
    if olf_file != new_file:
        with open(new_file, "w") as f_1, open(olf_file, "r") as f_2:
            f_1.write(f_2.read())
