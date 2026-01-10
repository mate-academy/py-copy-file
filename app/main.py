import shutil


def copy_file(file_to_copy: str) -> None:
    files = file_to_copy.split()
    if len(files) != 3 or files[0] != "cp":
        return
    second_file = files.pop()
    first_file = files.pop()

    if first_file == second_file:
        return

    try:
        shutil.copy(first_file, second_file)
    except Exception as e:
        print(e)
