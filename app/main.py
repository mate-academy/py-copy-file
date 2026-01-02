def copy_file(command: str) -> None:
    new_command = command.split()
    if len(new_command) != 3:
        return
    if new_command[0] != "cp":
        return
    src = new_command[1]
    dst = new_command[2]
    if src == dst:
        print("Source and destination are the same.")
        return
    try:
        with open(src, "r") as file_in, open(dst, "w") as file_out:
            file_out.write(file_in.read())
    except FileNotFoundError:
        return
