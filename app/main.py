import os


def copy_file(command: str) -> None:
    arguments = command.split(" ")
    if len(arguments) != 3:
        return
    command, src, dst = arguments

    if (
            command != "cp"
            or src == dst
            or not src
            or not dst
            or not os.path.exists(src)
    ):
        return
    with open(dst, "w") as dist_file, open(src, "r") as src_file:
        dist_file.write(src_file.read())
