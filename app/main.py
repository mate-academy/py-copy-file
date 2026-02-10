import shutil


def copy_file(command: str) -> None:
    new_name = command.split()
    try:
        if (len(new_name) >= 3
                and new_name[1] != new_name[2]
                and new_name[0] == "cp"):
            shutil.copy2(new_name[1], new_name[2])
    except FileNotFoundError:
        pass
