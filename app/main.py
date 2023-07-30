def copy_file(command, file_out, file_in: str) -> None:
    #did I understand correctly?
    if len(command.split()) == 3:
        command, file_out, file_in = command.split()
        if command == "cp" and file_out != file_in:
            with open(file_out, "r") as file_from, open(file_in, "w") as file_to:
                file_to.write(file_from.read())
