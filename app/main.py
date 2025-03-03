def copy_file(command: str) -> None:
    command = command.split(" ")
    if len(command) != 3 or command[0] != "cp":
        return
    open_file = command[1]
    save_file = command[2]
    if open_file == save_file:
        return
    try:
        with (open(open_file, "r") as file_in
            , open(save_file, "w") as file_out):
            file_out.write(file_in.read())
    except FileNotFoundError:
        pass
