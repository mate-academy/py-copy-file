import shutil


def copy_file(command: str) -> None:
    if len(command.split()) == 3 and command.split()[0] == "cp":
        _, filename1, filename2 = command.split()
        if filename1 == filename2:
            return
        try:
            shutil.copy(filename1, filename2)
        except FileNotFoundError:
            return
