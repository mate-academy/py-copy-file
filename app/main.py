def copy_file(command: str) -> None:
    cmd, old_file, new_file = command.split()
    if cmd == "cp" and old_file != new_file:
        with (
            open(old_file, "r") as old_file,
            open(new_file, "w") as new_file
        ):
            new_file.write(old_file.read())
