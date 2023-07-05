import shutil


def copy_file(argument: str) -> tuple:
    if len(argument.rsplit(" ")) == 3:
        src_path = argument.rsplit(" ")[1]
        dst_path = argument.rsplit(" ")[2]
        if src_path != dst_path:
            shutil.copy(src_path, dst_path)
            print("Copied")
            if open(src_path).read() == open(dst_path).read():
                return
