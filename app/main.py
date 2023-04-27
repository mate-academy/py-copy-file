def copy_file(command: str) -> None:
    if len(command.split()) != 3:
        raise ValueError("command should have 3 arguments")
    src_file_path = command[1]
    dst_file_path = command[2]
    if src_file_path == dst_file_path:
        raise TypeError
    with open(src_file_path, "r") as file_in,\
            open(dst_file_path, "w") as file_out:
        file_in.write(file_out.read())
