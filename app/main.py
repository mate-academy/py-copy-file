def copy_file(command: str) -> None:
    split_command = command.split()

    if len(split_command) < 3:
        return

    if "cp" != split_command[0]:
        return

    if split_command[1] == split_command[2]:
        return

    try:
        with (open(split_command[1], "r") as file_in,
              open(split_command[2], "w") as file_out):
            for line in file_in:
                file_out.write(line)
    except FileNotFoundError:
        return
