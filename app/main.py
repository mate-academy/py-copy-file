def copy_file(command: str) -> None:
    command = command.split()
    if len(command) == 3 and command[0] == "cp":
        with (
            open(command[1], "r") as read_file,
            open(command[2], "w") as write_file
        ):
            write_file.write(read_file.read())
        return
    print("Invalid command")
