def copy_file(command: str) -> None:
    if len(command) == 0:
        return
    list_command = command.split(" ")
    if len(list_command) != 3 or list_command[0] != "cp":
        return
    if list_command[1] == list_command[2]:
        return

    first_file = list_command[1]
    new_file = list_command[2]

    try:
        with open(first_file, "rb") as file_in, \
             open(new_file, "wb") as file_out:
            file_out.write(file_in.read())
    except FileNotFoundError:
        return
