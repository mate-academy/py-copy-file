def copy_file(command: str) -> None:
    list_from_command = command.split(" ")
    if len(list_from_command) != 3:
        return
    if list_from_command[0] != "cp":
        return
    if list_from_command[1] == list_from_command[2]:
        return
    with open(list_from_command[1], "r") as file_in, open(
        list_from_command[2], "w"
    ) as file_out:
        file_out.write(file_in.read())
