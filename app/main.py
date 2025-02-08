def copy_file(command: str) -> None:

    list_command = command.split()
    if len(list_command) != 3 and list_command[0] != "cp":
        return None
    if list_command[1] == list_command[2]:
        return None

    with (open(list_command[1]) as first_file,
          open(list_command[2], "w") as second_file):
        second_file.write(first_file.read())
