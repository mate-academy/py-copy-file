def copy_file(command: str) -> None:
    if not command.startswith("cp"):
        return

    command_split = command.split()
    if len(command_split) != 3:
        return

    _, from_file, to_file = command_split

    if from_file == to_file:
        return

    with open(from_file, "r") as file_in, open(to_file, "w") as file_out:
        for line in file_in:
            file_out.write(line)
