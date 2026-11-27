import shutil


def copy_file(command: str) -> None:
    command_parts = command.split()
    if (not len(command_parts) == 3
            or command_parts[0] != "cp"):
        return
    source_file = command_parts[1]
    file_copy = command_parts[2]
    if source_file == file_copy:
        return
    try:
        with (open(source_file, "r") as file_in,
              open(file_copy, "w") as file_out):
            shutil.copyfileobj(file_in, file_out)
    except FileNotFoundError:
        return
