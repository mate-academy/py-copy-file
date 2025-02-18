def copy_file(command: str) -> None:
    command = command.split()

    if len(command) != 3 or command[0] != "cp":
        raise Exception("Invalid command")

    _, exist_file_name, copy_file_name = command

    if exist_file_name != copy_file_name:
        with (
            open(exist_file_name, "r") as file,
            open(copy_file_name, "w") as copy
        ):
            copy.write(file.read())
