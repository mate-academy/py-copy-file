def copy_file(command: str) -> None:

    command = command.split()
    if len(command) != 3:
        return
    cur_file = command[1]
    new_file = command[2]

    if cur_file == new_file or command[0] != "cp":
        return

    try:
        with open(cur_file) as file_in, open(new_file, "w") as file_out:
            file_out.write(file_in.read())
    except FileNotFoundError:
        return
