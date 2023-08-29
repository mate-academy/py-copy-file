def copy_file(command: str) -> None:
    in_command = command.split()

    if len(in_command) != 3:
        raise SyntaxError("Wrong format of command")

    _, file, new_file = in_command

    if file != new_file:
        with open(file, "r") as file_in, open(new_file, "w") as file_out:
            content = file_in.read()
            file_out.write(content)
