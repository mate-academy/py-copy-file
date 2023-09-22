import shutil


def copy_file(command: str) -> None:
    content = command.split()
    if content[1] != content[2]:
        with open(content[1], "rb") as src_file, \
                open(content[2], "wb") as dest_file:
            shutil.copyfileobj(src_file, dest_file)
