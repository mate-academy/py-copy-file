# write your code here
import shutil


def copy_file(command: str) -> None:
    if command.startswith("cp "):
        cmd = command.split()
        old_path = cmd[1]
        new_path = cmd[2]
        if old_path != new_path:
            shutil.copy(old_path, new_path)
