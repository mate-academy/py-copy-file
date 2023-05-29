def copy_file(command: str) -> None:
    try:
        cmd, source_file, target_file = command.split()
    except ValueError:
        print("Command must have 2 arguments")
        return
    if cmd != "cp" or source_file == target_file:
        return

    with open(source_file, "r") as source, open(target_file, "w") as target:
        target.write(source.read())
