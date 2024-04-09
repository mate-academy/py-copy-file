def copy_file(command: str) -> None:
    command_split = command.split()
    if len(command_split) == 3:
        comm, old_file, new_file = command_split

    if old_file != new_file and comm == "cp":
        with (open(old_file, "r") as from_file,
              open(new_file, "w") as to_file):
            to_file.write(from_file.read())
