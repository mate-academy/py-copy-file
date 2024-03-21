def copy_file(command: str) -> None:

    command_name, file_name, file_copy = command.split()

    if command_name != "cp":
        return

    with (open(file_name, "r") as original,
            open(file_copy, "w") as copy):
        copy.write(original.read())
