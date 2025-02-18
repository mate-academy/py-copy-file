def copy_file(command: str) -> None:
    if len(command.split()) != 3:
        raise ValueError("cp command can take only 2 arguments")
    cp_command, file, new_file = command.split()
    if cp_command != "cp":
        raise ValueError("cp command not found")

    if file != new_file:
        with open(file, "r") as input_file, open(new_file, "w") as output_file:
            output_file.write(input_file.read())
