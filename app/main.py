import shutil


def copy_file(command: str) -> None:
    files = command.split()
    if len(files) != 3 or files[0] != "cp":
        return
    target_file = files.pop()
    source_file = files.pop()

    if source_file == target_file:
        return

    try:
        shutil.copy(source_file, target_file)
    except Exception as e:
        print(e)
