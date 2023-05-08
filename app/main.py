def copy_file(command: str) -> None | str:
    if len(command.split()) != 3:
        return "Incorrect command is printed"
    cmd, source_path, destination_path = command.split()
    if cmd != "cp":
        return "Command is not exist"
    if source_path == destination_path:
        return "The name of copied file is the same as original name"
    with open(source_path, "r") as original, open(
        destination_path, "w"
    ) as copied:
        copied.write(original.read())
