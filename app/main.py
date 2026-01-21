def copy_file(command: str) -> None:
    copy_command, original, copy = command.split()
    if copy_command == "cp" and original != copy:
        with open(original, "r") as file_in, open(copy, "w") as copy:
            copy.writelines(file_in.readlines())
