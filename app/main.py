import os
import shutil


def copy_file(source: str, destination: str) -> None:
    if not source or not destination:
        return
    
    if not os.path.exists(source) or not os.path.isfile(source):
        return

    if os.path.isdir(destination):
        destination = os.path.join(destination, os.path.basename(source))
    else:
        dest_dir = os.path.dirname(destination)
        if dest_dir and not os.path.exists(dest_dir):
            os.makedirs(dest_dir, exist_ok=True)

    shutil.copy(source, destination)


if __name__ == "__main__":
    pass

