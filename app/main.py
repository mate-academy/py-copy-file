def copy_file(command: str) -> None:
    command, old_file, new_file = command.split()

    if command == "cp" and old_file != new_file:
        with (open(old_file, "r") as old_file,
              open(new_file, "w") as new_file):
            new_file.write(old_file.read())
