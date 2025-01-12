# write your code here
import shutil


def copy_file(command: str) -> None:
    old_path = command.split()[1]
    new_path = command.split()[2]
    if old_path != new_path:
        shutil.copy(old_path, new_path)
