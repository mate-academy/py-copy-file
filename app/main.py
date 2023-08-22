def copy_file(command: str) -> None:
    command = command.split()

    if command[1] == command[2] and command[0] == "cp":
        return

    with open(command[1], "r") as file_in, open(command[2], "w") as file_out:
        content = file_in.read()
        file_out.write(content)
