def copy_file(command: str) -> None:
    copy, file, new_file = command.split()
    if file != new_file and copy == "cp":
        with open(file, "r") as file_1, open(new_file, "w") as file_2:
            file_2.write(file_1.read())
