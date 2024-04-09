def copy_file(command: str) -> None:
    if len(command.split()) == 3:
        old_file, new_file = command.split()[1:]

    if old_file != new_file:
        with (open(old_file, "r") as from_file,
              open(new_file, "w") as to_file):
            to_file.write(from_file.read())
