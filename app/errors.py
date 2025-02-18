class CopyCommandError(Exception):
    pass


class InvalidCommandError(CopyCommandError):
    pass


class SameFileError(CopyCommandError):
    pass
