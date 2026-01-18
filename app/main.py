import os


def copy_file(command: str) -> None:
    try:
        file_1, file_2 = command.replace("cp ", "").split()
    except ValueError:
        return
    if file_1 == file_2:
        return
    if file_1 not in os.listdir():
        return

    with open(file_1, "r") as file, open(file_2, "w") as file_coppy:
        file_coppy.write(file.read())
