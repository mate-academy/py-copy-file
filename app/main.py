import shutil


def copy_file(com: str) -> None:
    files = com.split()
    if len(files) != 3 or files[0] != "cp":
        return
    f2 = files.pop()
    f1 = files.pop()

    if f1 == f2:
        return

    try:
        shutil.copy(f1, f2)
    except Exception as e:
        print(e)
