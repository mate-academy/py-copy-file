def copy_file(command: str) -> None:
    command, file_name, copy_name = command.split()
    if file_name != copy_name and command == "cp":
        with open(file_name, "r") as old, open(copy_name, "w") as new:
            new.write(old.read())
