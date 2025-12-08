def copy_file(command: str) -> None:
    if command == "":
        return
    new_command = command.split()
    if len(new_command) != 3:
        return
    if new_command[0] != "cp":
        return
    if new_command[1] == new_command[2]:
        return

    try:
        with (open(new_command[1], "r") as file_in,
              open(new_command[2], "w") as file_out):
            content = file_in.read()
            file_out.write(content)
    except FileNotFoundError:
        return
