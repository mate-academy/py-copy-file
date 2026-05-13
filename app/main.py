def copy_file(command: str) -> None:
    command_split = command.split()

    if len(command_split) != 3:
        return

    if command_split[0] != "cp":
        return

    source_file = command_split[1]
    target_file = command_split[2]

    if source_file == target_file:
        return

    try:
        with (open(source_file, "r") as file_old,
              open(target_file, "w") as file_new):
            for line in file_old:
                file_new.write(line)
    except FileNotFoundError:
        return
