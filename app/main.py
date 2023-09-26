from shutil import copyfile


def copy_file(command: str) -> None:
    original_copy_names = command[2:].split()
    if original_copy_names[0] != original_copy_names[1]:
        copyfile(original_copy_names[0], original_copy_names[1])
