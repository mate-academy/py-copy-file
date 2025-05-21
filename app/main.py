def copy_file(command: str) -> None:
    if not command.startswith("cp"):
        return

    split_command = command.split(" ")
    if len(split_command) != 3:
        return

    old_file = split_command[1]
    new_file = split_command[2]

    if old_file == new_file:
        return

    if not (old_file.endswith(".txt")) and (new_file.endswith(".txt")):
        return

    try:
        with open(old_file, "r") as old, open(new_file, "w") as new:
            for line in old.readlines():
                new.write(line)
    except FileNotFoundError:
        return
