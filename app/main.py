def copy_file(command: str) -> None:
    _, src, dst = command.split()
    if src != dst:
        with open(src, "r") as file_in, \
                open(dst, "w") as file_out:
            file_out.write(file_in.read())
