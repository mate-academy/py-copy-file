def copy_file(command: str) -> None:
    list_of_command = command.split(" ")
    if len(list_of_command) != 3 or list_of_command[0] != "cp":
        return
    last_file = list_of_command[1]
    new_file = list_of_command[2]
    if last_file == new_file:
        return
    try:
        with open(last_file, "r") as f, open(new_file, "w") as n:
            text = f.read()
            n.write(text)
    except FileNotFoundError:
        return
