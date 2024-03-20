def copy_file(command: str) -> None:
    command_split = command.split(" ")
    if command_split[0] != "cp":
        return
    file_name = command_split[1]
    file_copy = command_split[2]
    with (open(file_name, "r") as original,
            open(file_copy, "w") as copy):
        copy.write(original.read())

