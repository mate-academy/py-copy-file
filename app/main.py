def copy_file(command: str) -> None:
    split_command = (command[3:-1] + "t").split(" ")
    name_to_search = split_command[0]
    name_to_copy = split_command[1]
    if name_to_copy == name_to_search:
        return
    with open(f"{name_to_search}", "r") as source:
        with open(f"{name_to_copy}", "w") as receiver:
            receiver.write(source.read())
