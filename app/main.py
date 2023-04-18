def copy_file(command: str) -> None:
    command_line = command.split(" ")
    command, file_1, file_2 = command_line
    if file_1 != file_2 and command == "cp":
        with open(file_1, "r") as file_in, open(file_2, "w") as file_out:
            date = file_in.read()
            file_out.write(str(date))
