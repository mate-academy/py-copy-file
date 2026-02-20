import os


def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) == 3 and parts[0] == "cp":
        file_src = parts[1]
        file_dst = parts[2]
        if file_src == file_dst:
            return
        try:
            if not os.path.isfile(file_src):
                return
            with (open(file_src, "r") as file_in,
                  open(file_dst, "w") as file_to):
                content = file_in.read()
                file_to.write(content)
        except OSError:
            return None
    return None
