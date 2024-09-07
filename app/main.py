def copy_file(command: str) -> None:
    command = command.split()
    if len(command) != 3 or command[0] != "cp":
        raise Exception("Invalid command")

    _, source_file_name, file_copy_name = command

    if source_file_name != file_copy_name:
        with (
            open(source_file_name, "r") as source_file,
            open(file_copy_name, "w") as file_copy
        ):
            file_copy.write(source_file.read())
