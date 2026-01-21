BUFFER_SIZE = 2048


def copy_file(user_command: str) -> None:
    command = user_command.split()

    if len(command) != 3 or \
            command[0].lower() != "cp" or \
            command[1] == command[2]:
        return

    with open(command[1], "rb") as src_obj, open(command[2], "wb") as dest_obj:
        buffer = src_obj.read(BUFFER_SIZE)
        while buffer:
            dest_obj.write(buffer)
            buffer = src_obj.read()


if __name__ == "__main__":
    copy_file("cp test1.txt test2.txt")
    copy_file("cp file.txt new_file.txt")
