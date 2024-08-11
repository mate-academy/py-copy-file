class InvalidCommandCp(Exception):
    """Command 'cp' is invalid.
    This command should look like this :
    'cp source_file.txt target_file.txt'"""


class IdenticalFileNames(Exception):
    """The source and target names files are identical. Does nothing."""
