import os


def copy_file(command: str) -> None:
    if len(command.split()) != 3:
        return
    cmd, src, dst = command.split()
    if cmd != "cp" or src == dst:
        return

    if os.path.basename(src) != src or os.path.basename(dst) != dst:
        return
    try:
        with open(src, "r") as file_in, open(dst, "w") as file_out:
            for line in file_in:
                file_out.write(line)
    except FileNotFoundError:
        return
