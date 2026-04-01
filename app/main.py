def copy_file(command: str) -> None:

    if not command:
        return

    command_list = command.split()

    if len(command_list) != 3:
        return

    if command_list[0] != "cp":
        return

    filename = command_list[1]
    new_filename = command_list[2]

    if filename == new_filename:
        return

    try:
        with open(filename, "r") as f, open(new_filename, "w") as n:
            content = f.read()
            n.write(content)

    except FileNotFoundError:
        return
