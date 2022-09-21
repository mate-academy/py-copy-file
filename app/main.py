def copy_file(command: str) -> None:
    command = command.split()[1:]
    if command[0] == command[1]:
        return None

    with open(command[0], "r") as file_in, open(command[1], "w") as file_out:
        for text in file_in.read():
            file_out.write(text)
