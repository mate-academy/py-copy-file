def copy_file(command: str) -> None:
    parameters = command.split()
    if len(command.split()) == 3:
        parameters = command.split()
    old_file = parameters[1]
    new_file = parameters[2]

    if (
            len(parameters) == 3
            and parameters[0] == "cp"
            and old_file != new_file
    ):
        with open(old_file, "r") as file_in, open(new_file, "w") as file_out:
            file_out.write(file_in.read())
