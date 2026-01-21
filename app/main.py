def copy_file(command: str):
    command_list = command.split(" ")
    perform_command = command_list[0]
    copy_from = command_list[1]
    copy_to = command_list[2]

    if perform_command == "cp" and copy_from != copy_to:
        with open(copy_from, mode="r") as read_file, \
                open(copy_to, mode="w") as written_file:
            for line in read_file:
                written_file.write(line)
