import shutil


def copy_file(command: str) -> None:
    split_command = command.split(" ")
    if len(split_command) == 3:
        if split_command[0] == "cp":
            src_file = split_command[1]
            dst_file = split_command[2]
            if src_file != dst_file:
                try:
                    with (open(src_file, "rb") as original,
                          open(dst_file, "wb") as copy):
                        shutil.copyfileobj(original, copy)
                except FileNotFoundError:
                    pass
