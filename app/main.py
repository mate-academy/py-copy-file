def copy_file(command_name: str) -> None:
    command_name = command_name.lower()
    command_tokens = command_name.split()

    if "" in command_tokens:
        for _ in range(command_tokens.count("")):
            command_tokens.remove("")

    if len(command_tokens) != 3:
        raise SyntaxError("File-copy command must consist of three tokens")
    if command_tokens[0] != "cp":
        raise SyntaxError("File-copy command is not recognized")
    if command_tokens[1] == command_tokens[2]:
        return

    with open(command_tokens[1], "r") as file_in, \
            open(command_tokens[2], "w") as file_out:
        for line in file_in:
            file_out.write(line)
