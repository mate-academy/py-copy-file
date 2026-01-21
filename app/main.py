import os


def copy_file(command: str) -> None:
    original_file, copy = command.split(" ")[1:]
    if original_file != copy:
        # os.popen("cp original_file copy") for Linux
        os.popen(f"copy {original_file} {copy}")
