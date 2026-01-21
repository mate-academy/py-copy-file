def copy_file(command: str) -> None:
    command_list = command.strip().split()
    if len(command_list) < 3:
        return  # Not anought arguments

    action = command_list[0]
    if action not in ("copy", "cp"):
        return None  # if action not support
    file_in = command_list[1]
    file_out = command_list[2]

    if file_in == file_out:
        return None  # Not copy

    try:
        with open(file_in, "r") as src, open(file_out, "w") as dst:
            content = src.read()
            dst.write(content)
    except (FileNotFoundError, OSError):
        return  # file not exit
