def copy_file(command: str) -> None:
    command, file, new_file = command.split("")
    if command == "cp":
        with open(file, "r") as source, open(new_file, "w") as target:
            data = source.read()
            target.write(data)
    if file == new_file:
        return
