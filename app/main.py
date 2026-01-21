def copy_file(command: str) -> None:
    cmd, src_file, dst_file = command.split(" ")

    if cmd != "cp" or src_file == dst_file:
        return

    with open(src_file, "r") as file_in, open(dst_file, "w") as file_out:
        file_out.write(file_in.read())
