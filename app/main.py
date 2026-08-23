def copy_file(command: str) -> None:

    list_command = command.split()

    if len(list_command) != 3:
        return
    elif list_command[1] == list_command[2]:
        return
    elif list_command[0] != "cp":
        return
    try:
        with open(list_command[1], "r") as file_in:
            file_in.read()
    except FileNotFoundError:
        return

    with (open(list_command[1], "r") as file_in,
          open(list_command[2], "w") as file_out):
        file_out.write(file_in.read())
