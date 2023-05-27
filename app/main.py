import shutil


def copy_file(command: str) -> None:
    _, src_file, dest_file = command.split()
    if src_file == dest_file:
        return

    with open(src_file, "r") as src, open(dest_file, "w") as dest:
        shutil.copyfileobj(src, dest)


copy_file("cp file.txt file.txt")
