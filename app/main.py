def copy_file(command: str) -> None:
    command = command.split(" ")
    name_from = command[1]
    name_to = command[2]
    if name_from == name_to:
        pass
    with open(name_from, "r") as file_in, open(name_to, "w") as file_out:
        file_out.write(file_in.read())
