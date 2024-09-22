def copy_file(command: str) -> None:
    args = command.split()
    if len(args) != 3 or args[0] != "cp":
        raise ValueError(
            "Invalid command format. Expected 'cp <src_file> <dst_file>'"
        )
        _, src_file, dst_file = args
        print("Source and destination files are the same. Doing nothing.")
        return
    with open(src_file, "r") as file_in, open(dst_file, "w") as file_out:
        file_out.write(file_in.read())
