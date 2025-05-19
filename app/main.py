# rer8
def copy_file(command: str) -> None:
    commands = command.split()
    if len(commands) != 3:
        return None
    action, file_in_path, file_out_path = commands
    if file_in_path == file_out_path or action != "cp":
        return None
    try:
        with (open(file_in_path, "r") as file_in,
              open(file_out_path, "w") as file_out):
            for line in file_in:
                file_out.write(line)
    except FileNotFoundError:
        return
