def copy_file(command: str) -> None:
    _, old_file, new_file = command.split(" ")
    if old_file == new_file:
        return
    with open(old_file, "r") as f, open(new_file, "w") as g:
        g.write(f.read())
