def copy_file(command: str) -> None:
    cmd, source_file, target_file = command.split()
    if cmd != "cp" or source_file == target_file:
        return
    try:
        with open(source_file, "r") as source, open(target_file, "w") as target:
            target.write(source.read())
    except UnicodeError:
        print("Error while copying file")
