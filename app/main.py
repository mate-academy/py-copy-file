def copy_file(command: str) -> None:
    command_line = command.split(" ")
    file_1 = command_line[1]
    file_2 = command_line[2]
    if file_1 == file_2:
        pass

    with open(file_1, "r") as file_in, open(file_2, "w") as file_out:
        date = file_in.read()
        file_out.write(str(date))
