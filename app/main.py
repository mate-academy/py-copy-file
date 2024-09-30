import shutil


def copy_file(command: str) -> None:
    cm, file, new_file = command.split(" ")
    if file == new_file:
        return
    if cm == "cp":
        with open(file, "r"), open(new_file, "w"):
            shutil.copyfile(file, new_file)
