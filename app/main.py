def cope_file(command: str) -> any:
    new_command = command.split()
    if new_command[1] == new_command[2]:
        return
    with open(new_command[1], "r") as file_in, open(new_command[2], "w"
                                                    ) as file_out:
        file_out.write(file_in.read())
