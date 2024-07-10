import shutil


def copy_file(source: str, destination: str) -> None:
    try:
        shutil.copy(source, destination)
    except shutil.SameFileError:
        print("Cannot copy the same file!")
    else:
        print("File has been copied successfully")
