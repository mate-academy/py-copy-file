import shutil

source = "/Users/jacktyler/py-copy-file/app/file.txt"
destination = "/Users/jacktyler/py-copy-file/app/new_file.txt"


def copy_file(source: str, destination: str) -> None:
    try:
        shutil.copy(source, destination)
    except shutil.SameFileError:
        print("Cannot copy the same file!")
    else:
        print("File has been copied successfully")


print(copy_file(source, destination))
