def copy_file(command: str) -> None:
    if len(command.split()) == 3:
        operation, file_1, file_2 = command.split()
    if operation == "cp" and file_1 != file_2:
        with open(file_1, "r") as file_in, open(file_2, "w") as file_out:
            file_out.write(file_in.read())
