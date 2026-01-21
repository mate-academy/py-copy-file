def copy_file(command: str) -> None:
    command_parts = command.split()
    if len(command_parts) != 3:
        return
    if command_parts[0] != "cp":
        return
    if command_parts[1] == command_parts[2]:
        return
    try:
        with (open(command_parts[1],
                   "r",
                  newline="",
                  encoding="utf-8") as file_read,
              open(command_parts[2],
                   "w",
                   newline="",
                   encoding="utf-8") as file_write):
            for line in file_read:
                file_write.write(line)
    except FileNotFoundError:
        return
