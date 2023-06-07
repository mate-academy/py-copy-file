def copy_file(command: str) -> None:
    command = command.split(" ")
    file_name = command[1]
    copy_file_name = command[2]
    with open(file_name, "r") as original, open(copy_file_name, "w") as copy:
        copy.write(original.read())
