def copy_file(command: str) -> None:
    command = command.split(" ")
    if len(command) != 3 or command[0] != "cp":
        return
    curr_file, new_file = command[1], command[2]
    if curr_file == new_file:
        return
    try:
        with open(curr_file, "r") as file_in, open(new_file, "w") as file_out:
            file_out.write(file_in.read())
    except FileNotFoundError:
        return
