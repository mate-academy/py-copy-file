import os


def copy_file(command: str) -> None:

    _, src_file, dst_file = command.split()

    if not os.path.exists(src_file):
        print(f"Error: {src_file} does not exist")
        return
    if os.path.exists(dst_file) and src_file == dst_file:
        return
    with open(src_file, "r") as f_src, open(dst_file, "w") as f_dst:
        f_dst.write(f_src.read())
