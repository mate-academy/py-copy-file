import shutil


def copy_file(command: str) -> None:
    file_names = command.replace("cp ", "").split(" ")
    if file_names[0] == file_names[1]:
        return
    shutil.copy(file_names[0], file_names[1])
