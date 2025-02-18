def copy_file(command: str) -> None:
    command_name, name_to_search, name_to_copy = command.split(" ")
    if command != "cp":
        raise NameError("The command does not exists")
    if name_to_copy == name_to_search:
        return
    with open(f"{name_to_search}", "r") as source:
        with open(f"{name_to_copy}", "w") as receiver:
            receiver.write(source.read())
