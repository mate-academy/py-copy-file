
def copy_file(command: str) -> None:
    tokens = command.split()
    if len(tokens) != 3:
        return
    if tokens[0] != "cp":
        return
    if tokens[1] == tokens[2]:
        return

    try:
        with open(tokens[1], "r") as file_in, open(tokens[2], "w") as file_out:
            for line in file_in.readlines():
                file_out.write(line)
    except FileNotFoundError:
        return
