def copy_file(command: str) -> None:
    if len(command.split()) < 3 or command.split()[0] != "cp":
        return
    old_file = command.split()[1]
    new_file = command.split()[2]
    if old_file == new_file:
        return
    try:
        with open(old_file, "r") as old, open(new_file, "w") as new:
            for line in old.readlines():
                new.write(line)
    except FileNotFoundError:
        print(f"No such file or directory: '{old_file}'")
