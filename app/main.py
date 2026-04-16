def copy_file(command: str = "cp") -> bool:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "cp":
        return False

    if parts[1] == parts[2]:
        return True

    try:
        with (open(parts[1], "r") as file_read,
              open(parts[2], "w") as file_write):
            for line in file_read.readlines():
                file_write.write(line)
    except FileNotFoundError:
        return False

    return True
