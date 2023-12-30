import shutil


def copy_file(command: str) -> None:
    command_file = command.split()
    src_f = command_file[1]
    dest_f = command_file[2]
    if src_f != dest_f:
        shutil.copy2(src_f, dest_f)
    else:
        return


if __name__ == "__main__":
    copy_file("cp file.txt file-copy.txt")
