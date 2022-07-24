def copy_file(command: str):
    command_list = command.split(" ")
    copy_from = command_list[1]
    copy_to = command_list[2]

    if copy_from != copy_to:
        with open(copy_from, mode="r") as read_file, \
                open(copy_to, mode="w") as written_file:
            for line in read_file:
                written_file.write(line)
