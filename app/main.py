def copy_file(command: str) -> None:
    command = command.split()
    from_file = command[1]
    to_file = command[2]
    if from_file != to_file:
        with open(from_file, "r") as file_in, open(to_file, "a") as file_out:
            file_out.write(file_in.read())
