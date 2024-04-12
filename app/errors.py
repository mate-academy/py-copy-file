class CopyFile(Exception):
    def __init__(self, cmd, file_1, file_2):
        self.cmd = cmd
        self.file_1 = file_1
        self.file_2 = file_2
        if cmd != "cp":
            raise WrongCommand(cmd)
        if file_1 == file_2:
            raise SameFile(file_1, file_2)


class WrongCommand(CopyFile):
    def __init__(self, cmd):
        self.cmd = cmd

    def __str__(self):
        return f"only \"cp\" command is supported"


class SameFile(CopyFile):
    def __init__(self, file_1, file_2):
        self.file_1 = file_1
        self.file_2 = file_2

    def __str__(self):
        return (f"Target file name should be different.\n"
                f"{self.file_1} can not exist with {self.file_2}\n"
                f"in the same directory")