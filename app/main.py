from app.errors import CopyFile


def copy_file(command: str) -> None:
    """
    this function designed for copying two files
    :param command: "cp file_to_copy.format new_file.format"
    """
    cmd, file_1, file_2 = command.split()
    try:
        CopyFile(cmd, file_1, file_2)
    except CopyFile:
        raise
    with open(file_1, "r") as file_in, open(file_2, "w") as file_out:
        file_out.write(file_in.read())
