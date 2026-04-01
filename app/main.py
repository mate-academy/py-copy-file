def copy_file(command: str) -> None:
    try:
        command = command.split()
        cur_file = command[1]
        new_file = command[2]
    except Exception:
        return
    if cur_file == new_file or len(command) != 3 or command[0] != "cp":
        return
    else:
        try:
            with open(cur_file), open(new_file, "w"):
                pass
        except FileNotFoundError:
            return
        else:
            with open(cur_file) as file_in, open(new_file, "w") as file_out:
                file_out.write(file_in.read())
