import os


def copy_file(command: str) -> None | ValueError | FileNotFoundError:
    """
    Mimics the Linux 'cp' command to copy a file from one location to another
    within the current directory. The function parses a string command, checks
    if the source and destination file names are different, and then copies
    the file's contents. If the source and destination files are the same,
    the function does nothing. It raises exceptions for invalid commands or
    if the source file does not exist.

    Parameters:
    -----------
    command : str
        A string representing the copy command,
        following the format 'cp <source> <destination>',
        where <source> is the file to be copied
        and <destination> is the target file name.

    Raises:
    -------
    ValueError:
        If the command is not in the expected 'cp <source> <destination>'.
    FileNotFoundError:
        If the source file does not exist in the current directory.

    Examples:
    ---------
    copy_file("cp file.txt new_file.txt")
        Copies the contents of 'file.txt' into 'new_file.txt'.

    copy_file("cp file.txt file.txt")
        Does nothing since the source and destination are the same.
    """

    parts = command.split(" ")
    if len(parts) != 3 or parts[0] != "cp":
        raise ValueError("Invalid format. Use: cp <source> <destination>")

    file_out, file_in = parts[1:]

    if file_out == file_in:
        return

    if not os.path.isfile(file_out):
        raise FileNotFoundError(f"The file '{file_out}' does not exist.")

    with open(file_out, "r") as from_file, open(file_in, "w") as to_file:
        to_file.write(from_file.read())
