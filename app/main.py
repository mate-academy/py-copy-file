def copy_file(command: str) -> None:
    split_command = command.split(" ")
    if command[0] != "cp":
        raise NameError("The command does not exists")
    name_to_search = split_command[1]
    name_to_copy = split_command[2]
    if name_to_copy == name_to_search:
        return
    with open(f"{name_to_search}", "r") as source:
        with open(f"{name_to_copy}", "w") as receiver:
            receiver.write(source.read())
