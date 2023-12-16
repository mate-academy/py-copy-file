def copy_file(command: str) -> None:
    cp_command, file_1, file_2 = command.split(" ")
    if file_1 == file_2 or cp_command != "cp":
        pass
    else:
        with open(file_1, "r") as source, open(file_2, "a") as target:
            for line in source:
                target.write(line)
