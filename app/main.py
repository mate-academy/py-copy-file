def copy_file(command: str) -> None:
    separated_command = command.split()
    if len(separated_command) != 3:
        raise ValueError("Your command is not valid")
    if separated_command[0] != "cp":
        raise ValueError("Use 'cp' at the beginning of command")
    file_from = separated_command[1]
    file_to = separated_command[2]
    if file_from != file_to:
        with open(file_from, "r") as file_from, open(file_to, "w") as file_to:
            data = file_from.read()
            file_to.write(data)
