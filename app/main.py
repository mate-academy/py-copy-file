def copy_file(command_line: str) -> None:
    command, src, dest = command_line.split(" ")
    if src == dest:
        return
    quantum = 8
    with open(src, "r") as read_src:
        with open(dest, "a") as write_dst:
            while True:
                current_read = read_src.read(quantum)
                if not current_read:
                    break
                write_dst.write(current_read)
