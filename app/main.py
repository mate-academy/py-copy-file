def copy_file(command: str) -> None:
    tokens = command.split()
    if tokens[0] != "cp" and len(tokens) != 3 and tokens[1] == tokens[2]:
        with open(tokens[1], "r") as file_in, \
                open(tokens[2], "w") as file_out:
            file_out.write(file_in.read())
