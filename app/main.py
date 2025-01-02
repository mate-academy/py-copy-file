def copy_file(command_line: str) -> None:
    arguments = command_line.split(" ")
    if not len(arguments) == 2:
        return
    command, src, dest = arguments
    if src == dest:
        return
    quantum = 8
    with open(src, "r") as read_src, open(dest, "w") as write_dst:
        while True:
            current_read = read_src.read(quantum)
            if not current_read:
                break
            write_dst.write(current_read)
