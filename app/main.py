def copy_file(command: str) -> None:
    args = command.split(" ")
    if args[1] == args[2] or args[0] != "cp":
        return
    with (open(args[1], "r") as file_read,
          open(args[2], "w") as file_write):
        buffer = file_read.read(256)
        while buffer:
            file_write.write(buffer)
            buffer = file_read.read(256)


copy_file("cp test.txt aboba.txt")
