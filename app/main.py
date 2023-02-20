def copy_file(command: str) -> None:
    command, file, new_file = command.split()
    if command == "cp" and file != new_file:
        with open(file, "r") as source, open(new_file, "w") as target:
            target.write(source.read())
