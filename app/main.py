def copy_file(command: str) -> None:
    _, from_file, to_file = command.split()

    if from_file == to_file:
        return

    with open(from_file, "r") as file_in, open(to_file, "w") as file_out:
        for line in file_in:
            file_out.write(line)
